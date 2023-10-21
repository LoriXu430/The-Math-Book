const express = require('express');
const passport = require('passport');
const LocalStrategy = require('passport-local').Strategy;
const jwt = require('jsonwebtoken');
const expressJwt = require('express-jwt');
const bcrypt = require('bcryptjs');

const app = express();
app.use(express.json());

const users = [
  { id: 1, username: 'user', password: '$2y$12$Wz8QX9zOjWYvT3tWu0zI/Oe7TPHsH/k.3zRkDnCySbB2.ZflY96O6' } // password is 'password'
];

passport.use(new LocalStrategy(
  function (username, password, done) {
    const user = users.find(u => u.username === username);
    if (!user) {
      return done(null, false);
    }
    bcrypt.compare(password, user.password, function (err, res) {
      if (res) {
        return done(null, { id: user.id, username: user.username });
      } else {
        return done(null, false);
      }
    });
  }
));

passport.serializeUser(function (user, done) {
  done(null, user.id);
});

passport.deserializeUser(function (id, done) {
  const user = users.find(u => u.id === id);
  done(null, user);
});

app.use(passport.initialize());

const secret = 'my_secret_key';

app.post('/login', passport.authenticate('local', { session: false }), (req, res) => {
  const token = jwt.sign({ id: req.user.id }, secret, { expiresIn: '1h' });
  res.json({ token });
});

const requireAuth = expressJwt({ secret, algorithms: ['HS256'] });

app.get('/profile', requireAuth, (req, res) => {
  res.json({ message: 'This is a protected route' });
});

app.listen(3000, () => {
  console.log('Server running on port 3000');
});

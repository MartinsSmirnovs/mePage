const { validate } = require('formee');

const myForm = document.querySelector('#foo');
const myRules = {
  // RegExp rule
  email: /.+\@.+\..+/,
};

myForm.onsubmit = function (ev) {
  ev.preventDefault();
  let errors = validate(myForm, myRules);
  if (myForm.isValid) return alert('Success!');
};
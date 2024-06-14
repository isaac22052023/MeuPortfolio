const lowercaseChars = "abcdefghijklmnopqrstuvwxyz";
const uppercaseChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
const numbersChars = "0123456789";
const symbolChars = "!-$+^";
const spacesChars = " ";

function getRandomChar(chars) {
  const index = Math.floor(Math.random() * chars.length);
  return chars[index];
}

function generatePassword() {
  const passwordInput = document.getElementById("password");
  const lowercaseCheckbox = document.getElementById("lowercase");
  const uppercaseCheckbox = document.getElementById("uppercase");
  const numbersCheckbox = document.getElementById("numbers");
  const symbolCheckbox = document.getElementById("symbols");
  const excludeDuplicateCheckbox = document.getElementById("exc-duplicate");
  const spacesCheckbox = document.getElementById("spaces");

  let characters = "";
  if (lowercaseCheckbox.checked) characters += lowercaseChars;
  if (uppercaseCheckbox.checked) characters += uppercaseChars;
  if (numbersCheckbox.checked) characters += numbersChars;
  if (symbolCheckbox.checked) characters += symbolChars;
  if (spacesCheckbox.checked) characters += spacesChars;

  if (characters === "") {
    passwordInput.value = "";
    return;
  }

  let password = "";
  const length = 12; // comprimento da senha padrão

  while (password.length < length) {
    let char = getRandomChar(characters);
    if (excludeDuplicateCheckbox.checked && password.includes(char)) continue;
    password += char;
  }

  passwordInput.value = password;
}

function copyPassword() {
  const passwordInput = document.getElementById('password');
  const copyButton = document.getElementById('copy');

  passwordInput.disabled = false;
  passwordInput.select();
  document.execCommand('copy');
  passwordInput.disabled = true;

  copyButton.textContent = 'Copiado';
  setTimeout(() => {
    copyButton.textContent = 'Copiar';
  }, 2000);
}

// Chamar a função generatePassword quando o botão de gerar senha é clicado
document.getElementById('generate-button').addEventListener('click', generatePassword);

// Chamar a função copyPassword quando o botão de copiar é clicado
document.getElementById('copy-button').addEventListener('click', copyPassword);
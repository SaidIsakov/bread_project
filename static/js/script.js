document.addEventListener("DOMContentLoaded", () => {
  setupFormValidation()
  setupNavigation()
})

function setupFormValidation() {
  const form = document.getElementById("contactForm")

  form.addEventListener("submit", (e) => {
    e.preventDefault()

    const name = document.getElementById("name").value.trim()
    const email = document.getElementById("email").value.trim()
    const phone = document.getElementById("phone").value.trim()
    const subject = document.getElementById("subject").value
    const message = document.getElementById("message").value.trim()

    // Валидация
    if (!name || !email || !phone || !subject || !message) {
      alert("Пожалуйста, заполните все поля")
      return
    }

    if (!isValidEmail(email)) {
      alert("Пожалуйста, введите корректный email")
      return
    }

    if (!isValidPhone(phone)) {
      alert("Пожалуйста, введите корректный номер телефона")
      return
    }

    // Формирование данных
    const formData = {
      name: name,
      email: email,
      phone: phone,
      subject: subject,
      message: message,
    }

    console.log("Форма отправлена:", formData)

    // Раскомментируйте для интеграции с Django:
    // fetch('/api/contact/', {
    //     method: 'POST',
    //     headers: {
    //         'Content-Type': 'application/json',
    //         'X-CSRFToken': getCookie('csrftoken')
    //     },
    //     body: JSON.stringify(formData)
    // })
    // .then(response => response.json())
    // .then(data => {
    //     alert('Спасибо! Мы вскоре свяжемся с вами');
    //     form.reset();
    // })
    // .catch(error => console.error('Ошибка:', error));

    alert("Спасибо за вашу заявку! Мы скоро с вами свяжемся.")
    form.reset()
  })
}

// Валидация email
function isValidEmail(email) {
  const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
  return regex.test(email)
}

// Валидация телефона
function isValidPhone(phone) {
  const regex = /^[\d\s\-+()]+$/
  return phone.length >= 10 && regex.test(phone)
}

// Навигация и мобильное меню
function setupNavigation() {
  const hamburger = document.getElementById("hamburger")
  const navLinks = document.querySelector(".nav-links")

  hamburger.addEventListener("click", () => {
    hamburger.classList.toggle("active")
    navLinks.classList.toggle("active")
  })

  // Закрытие меню при клике на ссылку
  document.querySelectorAll(".nav-links a").forEach((link) => {
    link.addEventListener("click", () => {
      hamburger.classList.remove("active")
      navLinks.classList.remove("active")
    })
  })
}

// Плавная прокрутка
function scrollToSection(sectionId) {
  const section = document.getElementById(sectionId)
  if (section) {
    section.scrollIntoView({ behavior: "smooth" })
  }
}

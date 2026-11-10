// ================================
// Registration Form JS
// ================================

// 1️⃣ File Upload Area & Image Preview
const fileUploadArea = document.getElementById('fileUploadArea');
const photoInput = document.getElementById('photo');
const previewContainer = document.getElementById('previewContainer');
const imagePreview = document.getElementById('imagePreview');
const removeImageBtn = document.getElementById('removeImage');

fileUploadArea.addEventListener('click', () => {
    photoInput.click();
});

photoInput.addEventListener('change', () => {
    const file = photoInput.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function (e) {
            imagePreview.src = e.target.result;
            previewContainer.classList.remove('hidden');
        };
        reader.readAsDataURL(file);
    }
});

removeImageBtn.addEventListener('click', () => {
    photoInput.value = '';
    imagePreview.src = '#';
    previewContainer.classList.add('hidden');
});

// Optional: Drag & Drop Support
fileUploadArea.addEventListener('dragover', (e) => {
    e.preventDefault();
    fileUploadArea.classList.add('drag-over');
});

fileUploadArea.addEventListener('dragleave', (e) => {
    e.preventDefault();
    fileUploadArea.classList.remove('drag-over');
});

fileUploadArea.addEventListener('drop', (e) => {
    e.preventDefault();
    fileUploadArea.classList.remove('drag-over');
    const files = e.dataTransfer.files;
    if (files.length) {
        photoInput.files = files;
        const event = new Event('change');
        photoInput.dispatchEvent(event);
    }
});

// 2️⃣ Password Show/Hide Toggle
const togglePassword = document.getElementById('togglePassword');
const passwordInput = document.getElementById('password');
togglePassword.addEventListener('click', () => {
    if (passwordInput.type === 'password') {
        passwordInput.type = 'text';
    } else {
        passwordInput.type = 'password';
    }
});

const toggleConfirmPassword = document.getElementById('toggleConfirmPassword');
const confirmPasswordInput = document.getElementById('confirm_password');
toggleConfirmPassword.addEventListener('click', () => {
    if (confirmPasswordInput.type === 'password') {
        confirmPasswordInput.type = 'text';
    } else {
        confirmPasswordInput.type = 'password';
    }
});

// 3️⃣ Password Match Checker
const passwordMatchIconCheck = document.querySelector('#passwordMatch .fa-check-circle');
const passwordMatchIconCross = document.querySelector('#passwordMatch .fa-times-circle');

function checkPasswordMatch() {
    if (!passwordInput.value || !confirmPasswordInput.value) {
        passwordMatchIconCheck.classList.add('hidden');
        passwordMatchIconCross.classList.add('hidden');
        return;
    }
    if (passwordInput.value === confirmPasswordInput.value) {
        passwordMatchIconCheck.classList.remove('hidden');
        passwordMatchIconCross.classList.add('hidden');
    } else {
        passwordMatchIconCheck.classList.add('hidden');
        passwordMatchIconCross.classList.remove('hidden');
    }
}

passwordInput.addEventListener('input', checkPasswordMatch);
confirmPasswordInput.addEventListener('input', checkPasswordMatch);

// 4️⃣ Optional: Checkbox toggle for "eligible_categories" visibility
const primaryCategorySelect = document.getElementById('primaryCategory');
const neutralCategoriesDiv = document.getElementById('neutralCategories');

primaryCategorySelect.addEventListener('change', () => {
    if (primaryCategorySelect.value) {
        neutralCategoriesDiv.classList.remove('hidden');
    } else {
        neutralCategoriesDiv.classList.add('hidden');
    }
});

import { CTAApi } from "./external-integration.js";

document.getElementById('subscriptionForm').addEventListener('submit', async function(event) {
    event.preventDefault();

    // Collecting all form values
    const name = document.getElementById('name').value.trim();
    const phone = document.getElementById('phone').value.trim();
    // const date = document.getElementById('date').value;
    // const time = document.getElementById('time').value;
    // const subscription = document.getElementById('subscription').value;
    const message = document.getElementById('message').value.trim();


    let isValid = true;

    // Reset error messages
    document.getElementById('nameError').textContent = '';
    document.getElementById('phoneError').textContent = '';
    document.getElementById('successMessage').style.display = 'none';
    document.getElementById('successMessage').textContent = '';
    document.getElementById('submitBtn').disabled = false;

    // Validation for name
    if (name === '') {
        document.getElementById('nameError').textContent = 'Name is required.';
        isValid = false;
    }

    // Validation for phone
    const phoneRegex = /^[0-9]{10}$/; // Example regex for a 10-digit phone number
    if (phone === '') {
        document.getElementById('phoneError').textContent = 'Phone number is required.';
        isValid = false;
    } else if (!phoneRegex.test(phone)) {
        document.getElementById('phoneError').textContent = 'Enter a valid 10-digit phone number.';
        isValid = false;
    }

     const recaptchaResponse = grecaptcha.getResponse();

     if (!recaptchaResponse) {
       document.getElementById("result").textContent =
         "Please complete the CAPTCHA";
       return;
     }
        

    // If form is valid, show success message and call API
    if (isValid) {
        const submitBtn = document.getElementById('submitBtn');
        const spinner = document.getElementById('spinner');
        const btnText = document.getElementById('btnText');

        submitBtn.disabled = true;
        spinner.style.display = 'inline-block'; // Show the spinner
        btnText.style.display = 'none'; // Hide the text

        // Mock API call with all collected data
        const formData = {
            name,
            phone,
            // date,
            // time,
            // subscription,
            message,
            recaptchaResponse
        };
        console.log(formData,"formData")

        try {
            // Send POST request to the API
            const response = await CTAApi(formData);
            console.log(response.ok,"response")
            if (response.ok) {
                document.getElementById('successMessage').style.display = 'block';
                document.getElementById('successMessage').className = 'success-message success';
                document.getElementById('successMessage').textContent = 'Form submitted successfully!';
            } else {
                document.getElementById('successMessage').style.display = 'block';
                document.getElementById('successMessage').className = 'success-message error';
                document.getElementById('successMessage').textContent = 'An error occurred while submitting the form. Please try again.';
            }
        } catch (error) {
            document.getElementById('successMessage').style.display = 'block';
            document.getElementById('successMessage').className = 'success-message error';
            document.getElementById('successMessage').textContent = 'An error occurred while submitting the form. Please try again.';
        } finally {
            document.getElementById('name').value='';
    document.getElementById('phone').value='';
    // document.getElementById('date').value='';
    // document.getElementById('time').value='';
    // document.getElementById('subscription').value='';
    document.getElementById('message').value='';
            submitBtn.disabled = false;
            spinner.style.display = 'none'; // Hide the spinner
            btnText.style.display = 'inline'; // Show the text again
        }
    }
});



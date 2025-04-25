document
  .getElementById("subscriptionForm")
  .addEventListener("submit", async function (event) {
    event.preventDefault();

    // Reset error messages
    document.getElementById("pincodeError").textContent = "";

    // Collect form values
    const name = document.getElementById("name").value.trim();
    const email = document.getElementById("email").value.trim();
    const phone = document.getElementById("phone").value.trim();
    const whatsapp = document.getElementById("whatsapp").value.trim();
    const city = document.getElementById("city").value.trim();
    const address = document.getElementById("address").value.trim();
    const pincode = document.getElementById("pincode").value.trim();

    let isValid = true;

    // Reset error messages
    document.getElementById("nameError").textContent = "";
    document.getElementById("phoneError").textContent = "";
    document.getElementById("whatsappError").textContent = "";
    document.getElementById("cityError").textContent = "";
    document.getElementById("addressError").textContent = "";
    document.getElementById("successMessage").style.display = "none";
    document.getElementById("successMessage").textContent = "";
    document.getElementById("pincodeError").textContent = "";

    // Validation for name
    if (name === "") {
      document.getElementById("nameError").textContent = "Name is required.";
      isValid = false;
    }
    // Validation for pincode
    const pincodeRegex = /^[0-9]{6}$/; // Regex for exactly 6 digits
    let finalPincode = pincode; // Default to user input
    if (pincode === "") {
      // If pincode is empty, set a default value for the backend
      finalPincode = "000000";
    } else if (!pincodeRegex.test(pincode)) {
      // If pincode is not valid, show an error message
      document.getElementById("pincodeError").textContent =
        "Pincode must be exactly 6 digits.";
      isValid = false;
    }

    if (!isValid) {
      return; // Stop form submission if validation fails
    }
    // Validation for phone
    const phoneRegex = /^[0-9]{10}$/; // Regex for exactly 10 digits
    if (phone === "") {
      document.getElementById("phoneError").textContent =
        "Phone number is required.";
      isValid = false;
    } else if (!phoneRegex.test(phone)) {
      document.getElementById("phoneError").textContent =
        "Enter a valid 10-digit phone number.";
      isValid = false;
    }

    // Validation for WhatsApp
    if (whatsapp === "") {
      document.getElementById("whatsappError").textContent =
        "WhatsApp number is required.";
      isValid = false;
    } else if (!phoneRegex.test(whatsapp)) {
      document.getElementById("whatsappError").textContent =
        "Enter a valid 10-digit WhatsApp number.";
      isValid = false;
    }

    // Validation for city
    if (city === "") {
      document.getElementById("cityError").textContent = "City is required.";
      isValid = false;
    }

    // Validation for address
    if (address === "") {
      document.getElementById("addressError").textContent =
        "Address is required.";
      isValid = false;
    }

    if (!isValid) {
      return; // Stop submission if validation fails
    }

    // Show loading spinner and disable the submit button
    const submitBtn = document.getElementById("submitBtn");
    const spinner = document.getElementById("spinner");
    const btnText = document.getElementById("btnText");

    submitBtn.disabled = true;
    spinner.style.display = "inline-block"; // Show the spinner
    btnText.style.display = "none"; // Hide the text

    // Prepare data to send to the API
    const formData = {
      name,
      email,
      phone,
      whatsapp,
      city,
      address,
      pincode: finalPincode, // Use the final pincode value
      contact: [
        {
          mobile_number: phone, // ✅ renamed from `phone`
          is_on_whatsapp: true, // ✅ must be true or false
        },
      ],
    };

    console.log("Form Data Sent to API:", formData); // Debugging

    try {
      // Send POST request to the API
      const response = await fetch(
        "https://app.carmaacarcare.com/api/admin/v1/garage-request-from-website",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjY3MzliODA1N2I5Y2FkNDFmYTI2NjcwNSIsImVtYWlsIjoiYXAzODQwNjlAZ21haWwuY29tIiwibmFtZSI6ImFua2l0IHBhdGVsIiwicGVybWlzc2lvbiI6W3sibW9kdWxlX2lkIjp7Il9pZCI6IjY3N2ZiYTAwM2ZlNjE1ZjVjYTBkOTgyNSIsInJvdXRlIjoiZGFzaGJvYXJkIiwiX192IjowLCJjcmVhdGVkQXQiOiIyMDI1LTAxLTA5VDExOjU4OjU1LjMzNloiLCJpY29uIjoiRGFzaGJvYXJkT3V0bGluZWQiLCJtb2R1bGVfbmFtZSI6IkRhc2hib2FyZCIsInByaW9yaXR5IjoiMSIsInVwZGF0ZWRBdCI6IjIwMjUtMDEtMDlUMTE6NTg6NTUuMzM2WiJ9LCJ2aWV3IjoiMCIsImVkaXQiOiIxIiwiX2lkIjoiNjc3ZmJiMTY1ZjhjN2MxN2Q1MmIxY2U4In0seyJtb2R1bGVfaWQiOnsiX2lkIjoiNjc3ZmJhMDAzZmU2MTVmNWNhMGQ5ODI2Iiwicm91dGUiOiJzZXJ2aWNlIiwiX192IjowLCJjcmVhdGVkQXQiOiIyMDI1LTAxLTA5VDExOjU4OjU1LjMzNloiLCJpY29uIjoiTG9jYWxDYXJXYXNoT3V0bGluZWQiLCJtb2R1bGVfbmFtZSI6IlNlcnZpY2VzIiwicHJpb3JpdHkiOiIyIiwidXBkYXRlZEF0IjoiMjAyNS0wMS0wOVQxMTo1ODo1NS4zMzZaIn0sInZpZXciOiIxIiwiZWRpdCI6IjEiLCJfaWQiOiI2NzdmYmIxNjVmOGM3YzE3ZDUyYjFjZTkifSx7Im1vZHVsZV9pZCI6eyJfaWQiOiI2NzdmYmEwMDNmZTYxNWY1Y2EwZDk4MjciLCJyb3V0ZSI6Im1hbmFnZS1hcHAtYmFubmVyIiwiX192IjowLCJjcmVhdGVkQXQiOiIyMDI1LTAxLTA5VDExOjU4OjU1LjMzNloiLCJpY29uIjoiSW1hZ2VPdXRsaW5lZCIsIm1vZHVsZV9uYW1lIjoiTWFuYWdlIEFwcCBCYW5uZXIiLCJwcmlvcml0eSI6IjMiLCJ1cGRhdGVkQXQiOiIyMDI1LTAxLTA5VDExOjU4OjU1LjMzNloifSwidmlldyI6IjEiLCJlZGl0IjoiMSIsIl9pZCI6IjY3N2ZiYjE2NWY4YzdjMTdkNTJiMWNlYSJ9LHsibW9kdWxlX2lkIjp7Il9pZCI6IjY3N2ZiYTAwM2ZlNjE1ZjVjYTBkOTgyOCIsInJvdXRlIjoidGVhbSIsIl9fdiI6MCwiY3JlYXRlZEF0IjoiMjAyNS0wMS0wOVQxMTo1ODo1NS4zMzZaIiwiaWNvbiI6Ikdyb3VwT3V0bGluZWQiLCJtb2R1bGVfbmFtZSI6IlRlYW0iLCJwcmlvcml0eSI6IjQiLCJ1cGRhdGVkQXQiOiIyMDI1LTAxLTA5VDExOjU4OjU1LjMzNloifSwidmlldyI6IjEiLCJlZGl0IjoiMSIsIl9pZCI6IjY3N2ZiYjE2NWY4YzdjMTdkNTJiMWNlYiJ9LHsibW9kdWxlX2lkIjp7Il9pZCI6IjY3N2ZiYTAwM2ZlNjE1ZjVjYTBkOTgyOSIsInJvdXRlIjoiY2l0eSIsIl9fdiI6MCwiY3JlYXRlZEF0IjoiMjAyNS0wMS0wOVQxMTo1ODo1NS4zMzZaIiwiaWNvbiI6IkxvY2F0aW9uQ2l0eU91dGxpbmVkIiwibW9kdWxlX25hbWUiOiJDaXR5IiwicHJpb3JpdHkiOiI1IiwidXBkYXRlZEF0IjoiMjAyNS0wMS0wOVQxMTo1ODo1NS4zMzZaIn0sInZpZXciOiIxIiwiZWRpdCI6IjEiLCJfaWQiOiI2NzdmYmIxNjVmOGM3YzE3ZDUyYjFjZWMifSx7Im1vZHVsZV9pZCI6eyJfaWQiOiI2NzdmYmEwMDNmZTYxNWY1Y2EwZDk4MmEiLCJyb3V0ZSI6InNlbmQtbm90aWZpY2F0aW9uIiwiX192IjowLCJjcmVhdGVkQXQiOiIyMDI1LTAxLTA5VDExOjU4OjU1LjMzNloiLCJpY29uIjoiTm90aWZpY2F0aW9uc0FjdGl2ZU91dGxpbmVkIiwibW9kdWxlX25hbWUiOiJTZW5kIE5vdGlmaWNhdGlvbiIsInByaW9yaXR5IjoiNiIsInVwZGF0ZWRBdCI6IjIwMjUtMDEtMDlUMTE6NTg6NTUuMzM2WiJ9LCJ2aWV3IjoiMSIsImVkaXQiOiIxIiwiX2lkIjoiNjc3ZmJiMTY1ZjhjN2MxN2Q1MmIxY2VkIn0seyJtb2R1bGVfaWQiOnsiX2lkIjoiNjc3ZmJhMDAzZmU2MTVmNWNhMGQ5ODJiIiwicm91dGUiOiJhcHAtY29udHJvbCIsIl9fdiI6MCwiY3JlYXRlZEF0IjoiMjAyNS0wMS0wOVQxMTo1ODo1NS4zMzZaIiwiaWNvbiI6IkFwcFJlZ2lzdHJhdGlvbk91dGxpbmVkIiwibW9kdWxlX25hbWUiOiJBcHAgQ29udHJvbCIsInByaW9yaXR5IjoiNyIsInVwZGF0ZWRBdCI6IjIwMjUtMDEtMDlUMTE6NTg6NTUuMzM2WiJ9LCJ2aWV3IjoiMSIsImVkaXQiOiIxIiwiX2lkIjoiNjc3ZmJiMTY1ZjhjN2MxN2Q1MmIxY2VlIn0seyJfaWQiOiI2N2YyMTk1NzE4ODg4NDE2Y2IxOTg5ODMiLCJtb2R1bGVfaWQiOnsiX2lkIjoiNjc4NzcwMjU1MzM0YzA2ZWQwOTAyN2Y0Iiwicm91dGUiOiJ1c2VycyIsIl9fdiI6MCwiY3JlYXRlZEF0IjoiMjAyNS0wMS0wOVQxMTo1ODo1NS4zMzZaIiwiaWNvbiI6IlN1cGVydmlzZWRVc2VyQ2lyY2xlT3V0bGluZWQiLCJtb2R1bGVfbmFtZSI6IlVzZXJzIiwicHJpb3JpdHkiOiI4IiwidXBkYXRlZEF0IjoiMjAyNS0wMS0wOVQxMTo1ODo1NS4zMzZaIn0sInZpZXciOiIxIiwiZWRpdCI6IjEifSx7Il9pZCI6IjY3ZjIxOTU3MTg4ODg0MTZjYjE5ODk4NCIsIm1vZHVsZV9pZCI6eyJfaWQiOiI2Nzg3YTZmMzUzMzRjMDZlZDA5MDI3ZmMiLCJyb3V0ZSI6ImJvb2tpbmdzIiwiX192IjowLCJjcmVhdGVkQXQiOiIyMDI1LTAxLTA5VDExOjU4OjU1LjMzNloiLCJpY29uIjoiUmVjZWlwdE91dGxpbmVkIiwibW9kdWxlX25hbWUiOiJCb29raW5ncyIsInByaW9yaXR5IjoiOSIsInVwZGF0ZWRBdCI6IjIwMjUtMDEtMDlUMTE6NTg6NTUuMzM2WiJ9LCJ2aWV3IjoiMSIsImVkaXQiOiIxIn0seyJfaWQiOiI2N2YyMTk1NzE4ODg4NDE2Y2IxOTg5ODUiLCJtb2R1bGVfaWQiOnsiX2lkIjoiNjc4Y2RmNDBlOTUwODk5MThjOTExZjM3Iiwicm91dGUiOiJwYXltZW50cyIsIl9fdiI6MCwiY3JlYXRlZEF0IjoiMjAyNS0wMS0wOVQxMTo1ODo1NS4zMzZaIiwiaWNvbiI6IlBheW1lbnRPdXRsaW5lZCIsIm1vZHVsZV9uYW1lIjoiUGF5bWVudHMiLCJwcmlvcml0eSI6IjEwIiwidXBkYXRlZEF0IjoiMjAyNS0wMS0wOVQxMTo1ODo1NS4zMzZaIn0sInZpZXciOiIxIiwiZWRpdCI6IjEifSx7Il9pZCI6IjY3ZjIxOTU3MTg4ODg0MTZjYjE5ODk4NiIsIm1vZHVsZV9pZCI6eyJfaWQiOiI2NzkyMzM0NzNhZWI0MWFiYTI5Njc3MDMiLCJyb3V0ZSI6ImNvdXBvbi1jb2RlcyIsIl9fdiI6MCwiY3JlYXRlZEF0IjoiMjAyNS0wMS0wOVQxMTo1ODo1NS4zMzZaIiwiaWNvbiI6IkRpc2NvdW50T3V0bGluZWQiLCJtb2R1bGVfbmFtZSI6Ik1hbmFnZSBDb3Vwb25zIiwicHJpb3JpdHkiOiIxMSIsInVwZGF0ZWRBdCI6IjIwMjUtMDEtMDlUMTE6NTg6NTUuMzM2WiJ9LCJ2aWV3IjoiMSIsImVkaXQiOiIxIn0seyJfaWQiOiI2N2YyMTk1NzE4ODg4NDE2Y2IxOTg5ODciLCJtb2R1bGVfaWQiOnsiX2lkIjoiNjc5Nzc3NGI0MjRhY2ZlNjAwZTc4MzZjIiwicm91dGUiOiJzdXJjaGFyZ2VzIiwiX192IjowLCJjcmVhdGVkQXQiOiIyMDI1LTAxLTA5VDExOjU4OjU1LjMzNloiLCJpY29uIjoiUGVyY2VudE91dGxpbmVkIiwibW9kdWxlX25hbWUiOiJNYW5hZ2UgU3VyY2hhcmdlIiwicHJpb3JpdHkiOiIxMiIsInVwZGF0ZWRBdCI6IjIwMjUtMDEtMDlUMTE6NTg6NTUuMzM2WiJ9LCJ2aWV3IjoiMSIsImVkaXQiOiIxIn1dLCJpYXQiOjE3NDM5MTk0NDcsImV4cCI6MTc0NzUxOTQ0N30.QNEhe892PoJD4iKUXH3eCc8Fm5rtOUqQk4WlQL6gQI4`,
          },
          body: JSON.stringify(formData),
        }
      );

      const responseData = await response.json();
      console.log("API Response:", responseData); // Debugging

      if (response.ok) {
        document.getElementById("successMessage").style.display = "block";
        document.getElementById("successMessage").className =
          "success-message success";
        document.getElementById("successMessage").textContent =
          "Form submitted successfully!";

        // Clear all input fields
        document.getElementById("subscriptionForm").reset();
      } else {
        // console.log(result.success);
        console.error("API Error:", response.status, response.statusText); // Debugging
        document.getElementById("successMessage").style.display = "block";
        document.getElementById("successMessage").className =
          "success-message error";
        document.getElementById("successMessage").textContent =
          responseData.message ||
          "An error occurred while submitting the form.";
      }
    } catch (error) {
      console.error("Network Error:", error); // Debugging
      document.getElementById("successMessage").style.display = "block";
      document.getElementById("successMessage").className =
        "success-message error";
      document.getElementById("successMessage").textContent =
        "A network error occurred. Please try again.";
    } finally {
      submitBtn.disabled = false;
      spinner.style.display = "none"; // Hide the spinner
      btnText.style.display = "inline"; // Show the text again
    }
  });

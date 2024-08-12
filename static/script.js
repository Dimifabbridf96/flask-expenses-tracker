setTimeout(function() {
    let message = document.querySelector('div.flash-message');
    message.style.display = 'none';
}, 5000);  // 5 seconds

document.addEventListener("DOMContentLoaded", function() {
    const relationSelect = document.getElementById("relation");
    const spouse1SalaryInput = document.getElementById("spouse1_salary");
    const spouse2SalaryInput = document.getElementById("spouse2_salary");
    const spouse1HoursInput = document.getElementById("spouse1_hour");
    const spouse2HoursInput = document.getElementById("spouse2_hour");
    const salaryInput = document.getElementById("salary");
    const HoursInput = document.getElementById("hour");
  
    relationSelect.addEventListener("change", function() {
      if (relationSelect.value === "Spouse 2 income") {
        spouse1SalaryInput.style.display = 'block';
        spouse2SalaryInput.style.display = 'block';
        spouse1HoursInput.style.display = 'block';
        spouse2HoursInput.style.display = 'block';
        salaryInput.style.display = 'none';
        HoursInput.style.display = 'none'
        salaryInput.previousElementSibling.style.display = 'none';
        HoursInput.previousElementSibling.style.display = 'none';
        spouse1SalaryInput.previousElementSibling.style.display = 'block'; // Show the label
        spouse2SalaryInput.previousElementSibling.style.display = 'block'; // Show the label
        spouse1HoursInput.previousElementSibling.style.display = 'block';
        spouse2HoursInput.previousElementSibling.style.display = 'block'; // Show the label
        spouse1SalaryInput.required = true;
        spouse2SalaryInput.required = true;
        salaryInput.required = false;
        HoursInput.required = false;
      } else {
        spouse1SalaryInput.style.display = 'none';
        spouse2SalaryInput.style.display = 'none';
        spouse1HoursInput.style.display = 'none';
        spouse2HoursInput.style.display = 'none';
        salaryInput.style.display = 'block';
        HoursInput.style.display = 'block';
        salaryInput.previousElementSibling.style.display = 'block';
        HoursInput.previousElementSibling.style.display = 'block'; // Show the label
        spouse1SalaryInput.previousElementSibling.style.display = 'none'; // Hide the label
        spouse2SalaryInput.previousElementSibling.style.display = 'none'; // Hide the label
        spouse1HoursInput.previousElementSibling.style.display = 'none';
        spouse2HoursInput.previousElementSibling.style.display = 'none';
        spouse1SalaryInput.required = false;
        spouse2SalaryInput.required = false;
        salaryInput.required = true;
        HoursInput.required = true;
      }
    });
  
    relationSelect.dispatchEvent(new Event("change"));
  });

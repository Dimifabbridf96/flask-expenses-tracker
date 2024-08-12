setTimeout(function() {
    let message = document.querySelector('div.flash-message');
    message.style.display = 'none';
}, 5000);  // 5 seconds

document.addEventListener("DOMContentLoaded", function() {
    const relationSelect = document.getElementById("relation");
    const spouse1SalaryInput = document.getElementById("spouse1_salary");
    const spouse2SalaryInput = document.getElementById("spouse2_salary");
    const salaryInput = document.getElementById("salary");
  
    relationSelect.addEventListener("change", function() {
      if (relationSelect.value === "Spouse 2 income") {
        spouse1SalaryInput.style.display = 'block';
        spouse2SalaryInput.style.display = 'block';
        salaryInput.style.display = 'none';
        salaryInput.previousElementSibling.style.display = 'none';
        spouse1SalaryInput.previousElementSibling.style.display = 'block'; // Show the label
        spouse2SalaryInput.previousElementSibling.style.display = 'block'; // Show the label 
      } else {
        spouse1SalaryInput.style.display = 'none';
        spouse2SalaryInput.style.display = 'none';
        salaryInput.style.display = 'block';
        salaryInput.previousElementSibling.style.display = 'block';
        spouse1SalaryInput.previousElementSibling.style.display = 'none'; // Hide the label
        spouse2SalaryInput.previousElementSibling.style.display = 'none'; // Hide the label
      }
    });
  
    relationSelect.dispatchEvent(new Event("change"));
  });

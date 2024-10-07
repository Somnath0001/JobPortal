document.addEventListener('DOMContentLoaded', function() {
    // Location toggle logic
    const existingLocationRadio = document.getElementById('existing-location');
    const newLocationRadio = document.getElementById('new-location');
    const jobLocationSelect = document.getElementById('job-location');
    const newAddressDiv = document.querySelector('.new-address');

    existingLocationRadio.addEventListener('change', function() {
        if (this.checked) {
            jobLocationSelect.style.display = 'block';
            newAddressDiv.style.display = 'none';
        }
    });

    newLocationRadio.addEventListener('change', function() {
        if (this.checked) {
            jobLocationSelect.style.display = 'none';
            newAddressDiv.style.display = 'block';
        }
    });

    // Initialize default state
    if (existingLocationRadio.checked) {
        jobLocationSelect.style.display = 'block';
        newAddressDiv.style.display = 'none';
    }

    // Dynamic skill box logic
    const skillSetCountSelect = document.getElementById('no-of-skill-set-required');
    const skillBoxContainer = document.querySelector('.skill-box-container');

    // Initialize skill box container
    skillBoxContainer.innerHTML = '';

    skillSetCountSelect.addEventListener('change', function() {
        const skillSetCount = parseInt(this.value);
        skillBoxContainer.innerHTML = '';

        for (let i = 0; i < skillSetCount; i++) {
            const skillBox = document.createElement('div');
            skillBox.className = 'input-box skill-box';

            skillBox.innerHTML = `
                <label for="required-skills-${i}">Skills Required ${i + 1}:</label>
                <div class="skill-fields">
                    <select id="required-skills-${i}" name="required-skills-${i}" required>
                        <option value="0">Java</option>
                        <option value="1">Python</option>
                        <option value="3">JavaScript</option>
                    </select>
                    <label for="required-skill-level-${i}">Skill Level:</label>
                    <select id="required-skill-level-${i}" name="required-skill-level-${i}" required>
                        <option value="1">Beginner</option>
                        <option value="2">Intermediate</option>
                        <option value="3">Advanced</option>
                        <option value="4">Expert</option>
                    </select>
                </div>
            `;

            skillBoxContainer.appendChild(skillBox);
        }
    });

    // Initialize default skill box
    skillSetCountSelect.dispatchEvent(new Event('change'));
});
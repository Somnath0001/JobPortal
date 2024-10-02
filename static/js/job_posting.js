// Get the skills select element
const skillsSelect = document.getElementById('required-skills');

// Get the skill level container
const skillLevelContainer = document.getElementById('skill-level-container');

// Add event listener to skills select element
skillsSelect.addEventListener('change', updateSkillLevels);

// Function to update skill levels
function updateSkillLevels() {
    // Clear existing skill level fields
    skillLevelContainer.innerHTML = '';

    // Get selected skills
    const selectedSkills = skillsSelect.selectedOptions;

    // Loop through each selected skill
    selectedSkills.forEach((skill) => {
        // Create a skill level select element
        const skillLevelSelect = document.createElement('select');
        skillLevelSelect.required = true;

        // Add skill level options
        const skillLevels = ['Beginner', 'Intermediate', 'Advanced', 'Expert'];
        skillLevels.forEach((level) => {
            const option = document.createElement('option');
            option.value = level;
            option.text = level;
            skillLevelSelect.appendChild(option);
        });

        // Create a label for the skill level select element
        const skillLabel = document.createElement('label');
        skillLabel.textContent = `${skill.value} Skill Level:`;

        // Append skill label and select element to container
        skillLevelContainer.appendChild(skillLabel);
        skillLevelContainer.appendChild(skillLevelSelect);
        skillLevelContainer.appendChild(document.createElement('br'));
    });
}

// Initial update
updateSkillLevels();
document.addEventListener('DOMContentLoaded', () => {
  const streakCountElement = document.getElementById('streak-count');
  const startStreakButton = document.getElementById('start-streak');

  let streak = 0;

  startStreakButton.addEventListener('click', () => {
    streak++;
    streakCountElement.textContent = streak;
    if (streak === 1) {
      startStreakButton.textContent = 'Add to Streak';
    }
  });
});

document.addEventListener("DOMContentLoaded", function() {
    const coinClicker = document.getElementById("coin");
    const coinCounter = document.getElementById("coin-counter");
    const profitPerTapElement = document.getElementById("profit-per-tap");
    const energyCounter = document.getElementById("energy-counter");
    let coins = parseInt(coinCounter.textContent);
    let profitPerTap = parseInt(profitPerTapElement.textContent);
    let energy = parseInt(energyCounter.textContent.split('/')[0]);

    coinClicker.addEventListener("click", function() {
        if (energy > 0) {
            coins += profitPerTap;
            energy -= 1;
            coinCounter.textContent = coins;
            energyCounter.textContent = `${energy}/1000`;
            updateServerCoins(coins);
        }
    });

    document.getElementById("upgrade-profit").addEventListener("click", function() {
        upgrade("profit");
    });

    document.getElementById("upgrade-energy").addEventListener("click", function() {
        upgrade("energy");
    });

    function updateServerCoins(coins) {
        fetch('/update_coins', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ coins: coins })
        });
    }

    function upgrade(type) {
        fetch('/upgrade', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ type: type })
        }).then(response => response.json())
          .then(data => {
              if (data.success) {
                  if (type === "profit") {
                      profitPerTap += 1;
                      profitPerTapElement.textContent = profitPerTap;
                  } else if (type === "energy") {
                      energy += 500;
                      energyCounter.textContent = `${energy}/1000`;
                  }
              }
          });
    }
});

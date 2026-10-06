console.log("app.js loaded");

// Form
const startupForm = document.getElementById("startupForm");

// Loading & Result
const loading = document.getElementById("loading");
const resultBox = document.getElementById("result");

// ------------------------------
// Helper Function
// ------------------------------
function fillList(id, items) {
    const list = document.getElementById(id);

    if (!list) return;

    list.innerHTML = "";

    if (!items || items.length === 0) {
        const li = document.createElement("li");
        li.textContent = "No data available.";
        list.appendChild(li);
        return;
    }

    items.forEach(item => {
        const li = document.createElement("li");
        li.textContent = item;
        list.appendChild(li);
    });
}

// ------------------------------
// Form Submit
// ------------------------------
startupForm.addEventListener("submit", async (event) => {

    event.preventDefault();

    console.log("Form submitted");

    // Collect Form Data
    const startupData = {
        startup_name: document.getElementById("startupName").value,
        startup_description: document.getElementById("startupDescription").value,
        industry: document.getElementById("industry").value,
        target_audience: document.getElementById("targetAudience").value,
        country: document.getElementById("country").value,
        business_stage: document.getElementById("businessStage").value,
        budget: document.getElementById("budget").value
            ? Number(document.getElementById("budget").value)
            : null
    };

    try {

        // Show loading
        loading.style.display = "block";
        resultBox.style.display = "none";

        const response = await fetch("http://127.0.0.1:8000/api/validate", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(startupData)
        });

        if (!response.ok) {
            throw new Error(`HTTP Error: ${response.status}`);
        }

        const result = await response.json();

        console.log("API Response:", result);
        console.log("Validation Score:", result.validation_score);

        loading.style.display = "none";
        resultBox.style.display = "block";

        alert("Step 1 - Response received");
        

        
        // Hide loading
        loading.style.display = "none";

        // -----------------------
        // Validation Score
        // -----------------------
        const score = result.validation_score || 0;

        alert("Step 2");

        const scoreValue = document.getElementById("scoreValue");
        const scoreFill = document.getElementById("scoreFill");

        scoreValue.textContent = `${score} / 100`;
        alert("Step 3");
        scoreFill.style.width = `${score}%`;

        // Reset previous classes
        scoreValue.className = "";

        // Default colour
        let colour = "#2563EB";

        if (score >= 90) {
            scoreValue.classList.add("score-excellent");
            colour = "#16A34A";
        }
        else if (score >= 75) {
            scoreValue.classList.add("score-good");
            colour = "#22C55E";
        }
        else if (score >= 60) {
            scoreValue.classList.add("score-average");
            colour = "#F59E0B";
        }
        else if (score >= 40) {
            scoreValue.classList.add("score-weak");
            colour = "#EA580C";
        }
        else {
            scoreValue.classList.add("score-poor");
            colour = "#DC2626";
        }

        scoreFill.style.backgroundColor = colour;

        alert("Step 4");

        // -----------------------
        // Main Sections
        // -----------------------
        document.getElementById("summary").textContent =
            result.summary || "No summary available.";

        document.getElementById("businessModelAnalysis").textContent =
            result.business_model_analysis || "No business model analysis available.";

        document.getElementById("revenueModelAnalysis").textContent =
            result.revenue_model_analysis || "No revenue model analysis available.";

        document.getElementById("marketSizeAnalysis").textContent =
            result.market_size_analysis || "No market size analysis available.";

        document.getElementById("problemSolutionFit").textContent =
            result.problem_solution_fit || "No problem–solution fit analysis available.";

        document.getElementById("competitiveAdvantageAnalysis").textContent =
            result.competitive_advantage_analysis || "No competitive advantage analysis available.";

        document.getElementById("investmentReadinessScore").textContent =
            (result.investment_readiness_score ?? 0) + "/100";

        document.getElementById("investmentReadinessAnalysis").textContent =
            result.investment_readiness_analysis || "No investment readiness analysis available.";

        document.getElementById("aiConfidenceScore").textContent =
            (result.ai_confidence_score ?? 0) + "/100";

        document.getElementById("aiConfidenceAnalysis").textContent =
            result.ai_confidence_analysis || "No AI confidence analysis available.";

        fillList("actionPlanList", result.action_plan);

        document.getElementById("marketOpportunity").textContent =
            result.market_opportunity || "No market opportunity available.";

        alert("Step 5");
        // -----------------------
        // SWOT
        // -----------------------
        fillList("strengthsList", result.strengths);

        fillList("weaknessesList", result.weaknesses);

        fillList("opportunitiesList", result.opportunities);

        fillList("threatsList", result.threats);

        // -----------------------
        // Risks
        // -----------------------
        fillList("risksList", result.risks);

        // -----------------------
        // Recommendations
        // -----------------------
        fillList("recommendationsList", result.recommendations);

        // Show Result
        resultBox.style.display = "block";

    }
    catch (error) {

        console.error("FULL ERROR:", error);

        alert(error.stack || error.message || error);

        loading.style.display = "none";
        resultBox.style.display = "none";
    }

});

alert("Step 6");
window.addEventListener('load', function () {
    const form_controls = document.querySelectorAll('.form-control');
    form_controls.forEach(fc => {
        fc.addEventListener('change', event => {
            // Get the form values
            const formData = new FormData(document.querySelector('#parameters-form'));
            const formJson = Object.fromEntries(formData.entries());
            const formJsonString = JSON.stringify(formJson);

            // Send the form values to server to run simulation
            fetch('/apps/pred-prey/run-simulation/', {
                method: 'POST',
                credentials: 'same-origin',
                body: formJsonString,
                headers: {
                    "X-CSRFToken": get_csrf_token(),
                    "Accept": "application/json",
                    "Content-Type": "application/json",
                }
            }).then(response => {
                if (!response.ok) {
                    console.error(`Error: ${response.status} ${response.statusText}`);
                }
                return response.json();
            }).then(json => {
                if (!json.success) {
                    console.error(`Error: ${json.error}`);
                }

                // Update the plots
                let popDynamicsFig = JSON.parse(json.pop_dynamics_fig);
                let popDynamicsPlotDiv = document.querySelector('#population-dynamics-container .plotly-graph-div');
                Plotly.react(popDynamicsPlotDiv, popDynamicsFig.data, popDynamicsFig.layout);
                let phaseSpaceFig = JSON.parse(json.phase_space_fig);
                let phaseSpacePlotDiv = document.querySelector('#phase-space-container .plotly-graph-div');
                Plotly.react(phaseSpacePlotDiv, phaseSpaceFig.data, phaseSpaceFig.layout);
            }).catch(
                error => console.error(`Error: ${error}`)
            );
        })
    });
});
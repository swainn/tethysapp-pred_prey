window.addEventListener('load', function () {
    // Trigger the window resize to fix the plot width issue
    window.dispatchEvent(new Event('resize'));

    // Prevent warning when leaving page
    window.onbeforeunload = null;

    // Load data
    const d = this.document.querySelector('#data');
    const scenario_data = JSON.parse(d.dataset.scenarios);

    // jQuery example: Bind event to the scenario select
    $('#scenario').on('change', function () {
        let selected_scenario = $('#scenario').val();
        let selected_scenario_data = scenario_data[selected_scenario];

        // Update form fields
        $('#alpha-input').val(selected_scenario_data.alpha);
        $('#beta-input').val(selected_scenario_data.beta);
        $('#delta-input').val(selected_scenario_data.delta);
        $('#gamma-input').val(selected_scenario_data.gamma);

        document.getElementById('alpha-input').dispatchEvent(new Event('change'));
    });
});
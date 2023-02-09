const ctx = 'fonny';
const myChart = new Chart(ctx, {
    type: "line",
    data: {
        labels: [],
        datasets: [{
            label: "f(x)",
            data: [],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)'
            ],
            borderWidth: 1,
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }

});

function handle(event) {
    event.preventDefault()
    myChart.data.labels = []
    myChart.data.datasets[0].data = []
    myChart.update()
    let f_input = document.getElementById("id_function").value
    let x_start = +document.getElementById("id_startfx").value;
    let x_end = +document.getElementById("id_endfx").value;
    let x_step = +document.getElementById("id_stepfx").value;
    console.log(typeof(x_start))

    with(Math) {
        try {
            var x = x_start
            while (x <= x_end) {

                console.log(f_input)
                var f = eval(f_input)
                console.log(f)
                myChart.data.labels.push(x)
                myChart.data.datasets[0].data.push(f)
                x += x_step
            }
        } catch (e) {
            if (e instanceof TypeError) {
                document.getElementById("error_message").innerHTML = "Error message: " + TypeError.message + " try other function";
            } else if (e instanceof ReferenceError) {
                document.getElementById("error_message").innerHTML = "Error message: " + ReferenceError.message + " try some other function";
            }
        }
    }

    myChart.update()
}
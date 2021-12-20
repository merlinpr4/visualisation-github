d3.csv("commits.csv").then(makeChart);

//make arrays out of the csv values
function makeChart(repos) {
  var reposLabels = repos.map(function (d) {
    return d.Repo;
  });
  var commitsData = repos.map(function (d) {
    return d.Commits;
  });

  console.log(reposLabels)
  console.log(commitsData)

//create a chart with the data collected
  var chart = new Chart("myChart", {
    type: "bar",
    data: {
      labels: reposLabels,
      datasets: [
        {
          label: "Total commits per repository",
          backgroundColor: "rgba(25,25,255,0.4)",
          data: commitsData, 
          borderWidth: 1
        }
      ]
    },
    

    
  });

}
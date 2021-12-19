d3.csv("commits.csv").then(makeChart);


function makeChart(repos) {
  var reposLabels = repos.map(function (d) {
    return d.Repo;
  });
  var commitsData = repos.map(function (d) {
    return d.Commits;
  });


  print(commitsData.toString)





  var chart = new Chart("myChart", {
    type: "horizontalBar",
    data: {
      labels: reposLabels,
      datasets: [
        {
          data: commitsData 
        }
      ]
    }
  });
}
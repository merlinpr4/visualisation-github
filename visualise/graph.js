d3.csv("commits.csv").then(makeChart);

//make arrays out of the csv values
function makeChart(repos) {
  var reposLabels = repos.map(function (d) {
    return d.Repo;
  });
  var commitsData = repos.map(function (d) {
    return d.Commits;
  });

  var languages = repos.map(function   (d){
   
     if (d.Language === "Java")
       return "#b07219";
     else if(d.Language === "Python")
       return "#3572A5";
     else if(d.Language === "CSS")
       return "#756bb1";
     else if(d.Language === "Ruby")
        return "#701516";
     else if (d.Language === "Javascript")
        return "#f1e05a";
     else if (d.Language === "R")
        return "#198ce7";
     else if (d.Language === "C")
        return  "#555555";
      else if (d.Language === "C++")
        return
      else if (d.Language === "PHP")
        return "#4F5D95"
      else if (d.Language === "Shell")
        return "#89e051";
      else if (d.Language === "TypeScript")
        return "#2b7489";
     else 
       return  'Green';

  });

// /**
//    * function to generate random color in hex form
//    */
//  function getRandomColorHex() {
//   var hex = "0123456789ABCDEF",
//       color = "#";
//   for (var i = 1; i <= 6; i++) {
//     color += hex[Math.floor(Math.random() * 16)];
//   }
//   return color;
// }



  console.log(reposLabels)
  console.log(commitsData)

//create a chart with the data collected
  var chart = new Chart("myChart", {
    type: "bar",
    options: {
      maintainAspectRatio: false,
      legend: {
        display: false
      },
      scales: {
        yAxes: [
          {
            scaleLabel: {
              display: true,
              labelString: "Total commits",
              fontSize: 16
            }
          }
        ]
      }
    },
    data: {
      labels: reposLabels,
      datasets: [
        {
          label: "Total commits per repository",
          backgroundColor: languages,
          data: commitsData, 
          borderWidth: 1
        }
      ]
    },
    

    
  });

}
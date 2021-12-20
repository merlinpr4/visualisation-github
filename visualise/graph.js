d3.csv("commits.csv").then(makeChart);

//make arrays out of the csv values
function makeChart(repos) {
  var reposLabels = repos.map(function (d) {
    return d.Repo;
  });
  var commitsData = repos.map(function (d) {
    return d.Commits;
  });

  
  let sum = 0;
  for(let i = 0 ; i < commitsData.length ; i ++) {
    console.log(commitsData[i]);
    sum += Number(commitsData[i]);
  }

console.log(sum);

  var descriptions = repos.map(function (d){
    return d.Descriptions;
  });

  var languages = repos.map(function (d) {
    return d.Language;
  });

  var languagesColor = repos.map(function   (d){
   
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




  console.log(reposLabels)
  console.log(commitsData)

//create a chart with the data collected
  var chart = new Chart("myChart", {
    type: "bar",
    data: {
      labels: reposLabels,
      datasets: [
        {
          label: "yo",
          backgroundColor: languagesColor,
          data: commitsData, 
          borderWidth: 1
        }
        
      ]
    },
    
      options: {
        responsive : true,
        maintainAspectRatio: true,
        legend: {
           position: 'bottom',
           display:  false  //fix this later 
        },
        title: {
          display: true,  
          text: "Total commits per repository"
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
        },

         // animation: true,
    // animationSteps: 60,

        // onClick: function(c,i){
        //     e = i[0];
        //   console.log("index",e._index)
        //   var x_value = this.data.labels[e._index];
        //   var y_value = this.data.datasets[0].data[e._index];
        //   console.log("x value",x_value);
        //   console.log("y value",y_value);
        //   },
       
        tooltips: {
          
          callbacks: {
            label: function(tooltipItem, data) {

              let line1 = "Total Commits: " + Number(tooltipItem.yLabel)  ;
            

              var numerator = commitsData[tooltipItem.index]
              var denominator =  sum ;
              var percent = Math.round((numerator/denominator) * 100)
              console.log(numerator)

              let line2 =  "Percentage: " + percent + "%";

              let line3 =  "Language: " + languages[tooltipItem.index] ; 

              return  [line1 ,line2,line3];
            },
            afterLabel: function(tooltipItem, data) {
     
              //let line4 =  "description: " + descriptions[tooltipItem.index] ; 
              return "" ;

             
            }
          }
        }
      }
  });

}
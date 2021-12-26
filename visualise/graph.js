d3.csv("commits.csv").then(makeChart);


//converting the csv values into an earier format for the charts to use
function makeChart(repos) {
  var reposLabels = repos.map(function (d) {
    return d.Repo;
  });
  var commitsData = repos.map(function (d) {
    return d.Commits;
  });

  var sizeData =  repos.map(function (d) {
    return d.Size;
  });

  var contributors =  repos.map(function (d) {
    return d.Contributors;
  });

  var daysData = repos.map(function(d){
    return d.Days;
  });

  console.log(daysData)


  // const scatterData = sizeData.map((x, i) => {
  //   return {
  //     x: x,
  //     y: commitsData[i]
  //   };
  // });

 //get the average commits  
  let sum = 0;
  for(let i = 0 ; i < commitsData.length ; i ++) {
    //console.log(commitsData[i]);
    sum += Number(commitsData[i]);
  }

  let avg = sum/commitsData.length;
  //console.log(avg);

  const horizontalLine = commitsData.map(x => avg);
  //console.log(horizontalLine);

//console.log(sum);

  var descriptions = repos.map(function (d){
    return d.Descriptions;
  });

  var languages = repos.map(function (d) {
    return d.Language;
  });

  var languagefreq = {};
  languages.forEach(function (x) { languagefreq[x] = (languagefreq[x] || 0) + 1; });
 // console.log(languagefreq) 


  var lang = [];
  var freq = [];
    for(x in languagefreq)
    {
      lang.push(x);
      freq.push(languagefreq[x])
    }

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

  
  var chart3 = new Chart("daysSpend", {
    type: 'line',
    data: {
      labels: reposLabels,
      datasets: [{
        label: "days",
        backgroundColor: "#3e95cd",
        data: daysData
      }]
    },
    options: {
      title: {
        display: true,
        text: 'Days spend on a repository'
      }
    }
});


var chart2 = new Chart("twoLineGraph", {
  type: "line",
  data: {
    labels: reposLabels,
    datasets: [{
      label: "commits",
      labelString: "Total Commits",
      yAxisID: "commits",
      data: commitsData,
      borderColor: "blue",
      fill: false
    },
      {
        label: "size",
        labelString: "Total Size(KB)",
        yAxisID: "size",
        data: sizeData,
        borderColor: "purple",
        fill: false
    }]
  },
  options: {
    legend: {
      display: true
    },
    scales: {
      yAxes: [{
        gridLines: {
          display:false
        },
        id: 'commits',
        labelString: "commits",
        type: 'linear',
        position: 'left',
         scaleLabel: {
          display: true,
          labelString: "Total Commits",
          fontSize: 16
        }
      },
      {
        id: 'size',
        type: 'linear',
        position: 'right',
        scaleLabel: {
          display: true,
          labelString: "Total Size",
          fontSize: 16
        }
      
      }]
    },
    title: {
      display: true,
      text: 'Total Commits vs Total Size'
  }
}
});


var chart3 = new Chart("primaryLanguageFrequency", {
  type: 'doughnut',
  data: {
    labels: lang,
    datasets: [
      {
        label: "Population (millions)",
        backgroundColor: ["#3e95cd", "#8e5ea2","#3cba9f","#e8c3b9","#c45850"],
        data: freq
      }
    ]
  },
  options: {
    title: {
      display: true,
      text: 'Most commonly used primary language'
    }
  }
});



//creats barchart of total commits per repo
  var chart = new Chart("totalCommits", {
    type: "bar",
    data: {
      labels: reposLabels,
      datasets: [
        {
          label: "Commits",
          legend : false ,
          backgroundColor:  languagesColor,
          data: commitsData,
          order:1 , 
          borderWidth: 1
        },
       {
          label: "Average Commits: " + avg,
          borderColor: "blue",
          data: horizontalLine , 
          borderDash : [5,5 ],
          pointRadius : 0 ,
          fill: false ,
          borderWidth: 1.5,
          type: "line",
          order:0
        }
      ]
    },
      options: {
        responsive : true,
        maintainAspectRatio: true,
        legend: {
           position: 'top',
           display:  true 
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
        tooltips: {
          callbacks: {
            label: function(tooltipItem, data) {
              let line1 = "Total Commits: " + Number(tooltipItem.yLabel)  ;
              //let line4 =  "description: " + descriptions[tooltipItem.index] ; 
              return line1 ;
             
            },
            afterLabel: function(tooltipItem, data) {
              var numerator = commitsData[tooltipItem.index]
              var denominator =  sum ;
              var percent = Math.round((numerator/denominator) * 100)
              console.log(numerator)
              let line2 =  "Percentage: " + percent + "%";
              let line3 = "Size in KB: " + sizeData[tooltipItem.index]; 
              let line4 = "Contributors" + contributors[tooltipItem.index];
              let line5 =  "Language: " + languages[tooltipItem.index] ;
              return  [line2 ,line3,line4,line5];
             
            }
          }
        }
      }
  });

}
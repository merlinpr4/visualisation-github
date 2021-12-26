
d3.csv("commits.csv").then(makeChart);
console.log("hiii")

var div = document.getElementById("user_info");
div.innerHTML += '';

d3.csv("user_info.csv", function(data) {
  div.innerHTML += "Username: " + data.Username  + "<br />" 
  div.innerHTML += "Name: " + data.Name  + "<br />" 
  div.innerHTML += "Public Repos: " + data.Repos  + "<br />" 

  div.innerHTML += "Followers: " + data.Followers + "<br />" 
  div.innerHTML += "Followings: " + data.Following + "<br />" 

  
  const img = document.getElementById("profile_pic");
  img.src = data.PP
});


//converting the csv values into a format for the charts to use
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

  var descriptions = repos.map(function (d){
    return d.Descriptions;
  });

 //get the average commits  
  let sum = 0;
  for(let i = 0 ; i < commitsData.length ; i ++) {
    sum += Number(commitsData[i]);
  }

  let avg = sum/commitsData.length;
  const horizontalLine = commitsData.map(x => avg);

  
  var languages = repos.map(function (d) {
    return d.Language;
  });

  //count freq of top language used
  var languagefreq = {};
  languages.forEach(function (x) { languagefreq[x] = (languagefreq[x] || 0) + 1; });
  var lang = [];
  var freq = [];
    for(x in languagefreq)
    {
      lang.push(x);
      freq.push(languagefreq[x])
    }


  //language color 
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

  
  //functions to load the graphs
  commitsChart(reposLabels,languagesColor,commitsData,avg,horizontalLine,sum,sizeData,contributors,languages,daysData)
  commitsVsSizeChart(reposLabels,commitsData,sizeData)
  languageChart(lang,freq)
  daysChart(reposLabels,daysData,commitsData)
}

//creats barchart of total commits per repo with extra info such as size,languages,contributors etc
function commitsChart(reposLabels,languagesColor,commitsData,avg,horizontalLine,sum,sizeData,contributors,languages,daysData){
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
            let line6 = "Days spend: " + daysData[tooltipItem.index];
            return  [line2 ,line3,line4,line5,line6];
           
          }
        }
      }
    }
});
}

//doughtnut chart of most commun languages used
function languageChart(lang,freq){
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
}

//linegraph of commits versus size in KB of all repos
function commitsVsSizeChart(reposLabels,commitsData,sizeData){
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
}

function daysChart(reposLabels,daysData,commitsData ){
var chart3 = new Chart("daysSpend", {
  type: 'bar',
  data: {
    labels: reposLabels,
    datasets: [{
      label: "days",
      backgroundColor: "#3e95cd",
      data: daysData
    },
    {
      label: "commits",
      backgroundColor: "green",
      data: commitsData 
    }
  ]
  },
  options: {
    title: {
      display: true,
      text: 'Days spend on repo vs total commits'
    }
  }
});
}
// @TODO: YOUR CODE HERE!

var svgWidth = 960;
var svgHeight = 500;

var margin = {
  top: 20,
  right: 40,
  bottom: 60,
  left: 100
};

var width = svgWidth - margin.left - margin.right;
var height = svgHeight - margin.top - margin.bottom;


var svg = d3.select('#scatter')
            .append('svg')
            .attr("width", svgWidth)
            .attr("height", svgHeight);
          
          
d3.csv('./assets/data/data.csv').then(function(data){

    var dataset = data.map((d) => {
        return [d.healthcare, d.poverty]
    })

    var x = d3.scaleLinear()
    .domain([8, 22])
    .range([ 0, width ]);
  svg.append("g")
    .attr("transform", "translate(0," + height + ")")
    .call(d3.axisBottom(x));

  // Add Y axis
  var y = d3.scaleLinear()
    .domain([0, 30])
    .range([ height, 0]);
  svg.append("g")
    .call(d3.axisLeft(y));

    svg.selectAll("circle")
    .data(dataset)
    .enter()
    .append("circle")
    .attr("cx", function(d) {
        return x(d[1]);
   })
   .attr("cy", function(d) {
        return y(d[0]);
   })
   .attr("r", 5);

})
          
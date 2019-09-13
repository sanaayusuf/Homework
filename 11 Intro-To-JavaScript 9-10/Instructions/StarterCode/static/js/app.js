// from data.js
var tableData = data;

// YOUR CODE HERE!
function addRow(data) {
    let keys = Object.keys(data);
    // Get a reference to the table
    let tableRef = document.getElementById('tbody');

    // Insert a row at the end of the table
    let newRow = tableRef.insertRow(-1);

    keys.forEach((key, index) => {
        // Insert a cell in the row at index
        let newCell = newRow.insertCell(index);

        // Append a text node to the cell
        let newText = document.createTextNode(data[key]);
        newCell.appendChild(newText);
    })
}

function clearRow(){
    const myNode = document.getElementById("tbody");
  while (myNode.firstChild) {
    myNode.removeChild(myNode.firstChild);
  }
}

tableData.forEach(data => addRow(data))

$(document).ready(function () {
    //your code here
    $('#datetime').on('input', function (event) {
        clearRow()
        const inputValue = event.target.value;
        if (inputValue.length) {
            const filteredData = tableData.filter((data) => data.datetime === inputValue)
            filteredData.forEach(data => addRow(data))
        } else {
            tableData.forEach(data => addRow(data))
        }
    });
});

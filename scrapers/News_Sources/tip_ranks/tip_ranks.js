const tipranksApi = require('tipranks-api-v2');
const fs = require('fs');
const path = require('path');

// tipranksApi.getPriceTargets('TSLA').then(result => console.log(result));
// tipranksApi.getNewsSentimentData('TSLA').then(result => console.log(result));
// tipranksApi.getTrendingStocks().then(trending => console.log(trending));


// Initialize an empty array to store symbols
const symbolsList = [];

// Specify the file path (absolute or relative)
const filePath = "marketcapTopCompanies.csv";

// Read the CSV file using the specified file path
fs.readFile(filePath, 'utf8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }

  // Split the data into rows
  const rows = data.split('\n');

  // Loop through each row of companies
  for (let i = 1; i < rows.length; i++) {
    const row = rows[i];
    const columns = row.split(',');

    // Extract the symbol from the columns array and add it to the symbols list
    const symbol = columns[2];
    symbolsList.push(symbol);
  }
  
  console.log(symbolsList);

});
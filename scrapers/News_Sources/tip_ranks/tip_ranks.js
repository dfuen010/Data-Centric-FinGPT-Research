const tipranksApi  = require('tipranks-api-v2');
const fs = require('fs');
const path = require('path');


// tipranksApi.getPriceTargets('AAPL').then(result => console.log(result));
// tipranksApi.getNewsSentimentData('TSLA').then(result => console.log(result));
// tipranksApi.getTrendingStocks().then(trending => console.log(trending));

async function main() {
    // Initialize an empty array to store symbols
    const symbolsList = [];
  
    // Specify the correct absolute file path
    const filePath = path.join(__dirname, 'marketcapTopCompanies.csv'); // Adjust the file path as needed
  
    try {


      // Read the CSV file using the specified file path
      const data = await fs.promises.readFile(filePath, 'utf8');
  
      // Split the data into rows
      const rows = data.split('\n');
  
      // Loop through each row of companies
      for (let i = 1; i < 11; i++) {
        const row = rows[i];
        const columns = row.split(',');
  
        // Extract the symbol from the columns array and add it to the symbols list
        const symbol = columns[2];
        symbol.trim();
        symbolsList.push(symbol);
      }
  
      //console.log(symbolsList);
      // Iterate through symbolsList and fetch information for each ticker
      for (const ticker of symbolsList) {
        try {
          tipranksApi.getPriceTargets(ticker).then(result => console.log(result));
          const newsSentiment = await tipranksApi.getNewsSentimentData(ticker);
  
          console.log(`Ticker: ${ticker}`);
          console.log('Price Targets:', priceTargets);
          console.log('News Sentiment:', newsSentiment);
          console.log('-------------------------------------------');
        } catch (error) {
          console.error(`Error fetching data for ticker ${ticker}:`, error);
        }
      }
    } catch (err) {
      console.error(err);
    }
  }
  
  // Call the main function
  main();
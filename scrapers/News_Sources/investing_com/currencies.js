const { investing } = require('investing-com-api');
// Import the fs module to write info into file.
const fs = require('fs').promises; 

async function main() {
  try {

    // id 1 stands for euro us currency comparison
    const currencyEUROtoUSD = await investing("1"); 
    // id 2 stands for british pounnd us currency comparison
    const currencyPOUNDtoUSD = await investing("2"); 
    // id 8827 for USD Index Futures
    const usDollarFutures = await investing("8827");

    // Convert Millisecond timestamp to regular date format
    const convertTimestampToDate = (timestamp) => {
      const date = new Date(timestamp);
      // Format as ISO date string (e.g., "2024-04-11T00:00:00.000Z")
      return date.toISOString(); 
    };

    // Convert timestamps in the API response to regular date format
    currencyEUROtoUSD.forEach(entry => {
      entry.date = convertTimestampToDate(entry.date);
    });

    currencyPOUNDtoUSD.forEach(entry => {
      entry.date = convertTimestampToDate(entry.date);
    });

    usDollarFutures.forEach(entry => {
      entry.date = convertTimestampToDate(entry.date);
    })

    // Convert responses to JSON with indentation
    const jsonContent = JSON.stringify({ currencyEUROtoUSD, currencyPOUNDtoUSD, usDollarFutures }, null, 4);

    // Write formatted JSON to a file
    await fs.writeFile('currency.txt', jsonContent);

    console.log('Responses written to currency.txt file.');

  } catch (err) {
    console.error(err);
  }

}


main();
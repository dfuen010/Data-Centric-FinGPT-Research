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
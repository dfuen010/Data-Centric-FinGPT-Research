const { investing } = require('investing-com-api');
const fs = require('fs').promises; // Import the fs module

async function main() {
  try {

    // id 8874 for Nasdaq Futures
    const NASDAQFutures = await investing("8874");
    // id 169 for Dow Jones Industrial Average Futures
    const DowJonesFutures = await investing("169");
    // id 8839 for S&P 500 Futures 
    const SP500Futures = await investing("8839");

    // Convert Millisecond timestamp to regular date format
    const convertTimestampToDate = (timestamp) => {
      const date = new Date(timestamp);
      // Format as ISO date string (e.g., "2024-04-11T00:00:00.000Z")
      return date.toISOString(); 
    };

    // Convert timestamps in the API response to regular date format
    NASDAQFutures.forEach(entry => {
      entry.date = convertTimestampToDate(entry.date);
    });

    DowJonesFutures.forEach(entry => {
      entry.date = convertTimestampToDate(entry.date);
    });

    SP500Futures.forEach(entry => {
      entry.date = convertTimestampToDate(entry.date);
    })

    // Convert responses to JSON with indentation
    const jsonContent = JSON.stringify({ NASDAQFutures, DowJonesFutures, SP500Futures }, null, 4);

    
    // Write formatted JSON to a file
    await fs.writeFile('futureResults.txt', jsonContent);

    console.log('Responses written to futureResults.txt file.');

  } catch (err) {
    console.error(err);
  }


}


main();




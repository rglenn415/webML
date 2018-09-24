function parseFeatures(files){
    //selects the first file
    //possible to send many files, but for now we will only use one
    var data = Papa.parse(files[0],{
        complete: function(results){
            console.log('finished', results.data[0]);

        }
    });
    console.log('in parseFeatures');
};
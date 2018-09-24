function parseFeatures(files){
    //selects the first file
    //possible to send many files, but for now we will only use one
    var data = Papa.parse(files[0],{
        complete: function(results){

            console.log('finished',results.data[0]);
            // return results.data[0];
            document.getElementById('featureSelect').style.visibility = 'visible';
            results.data[0].forEach(function(feature){
                //create element -> set element to user given feature->append element to html
                var option = document.createElement("option");
                option.innerHTML = feature;
                document.getElementById("featureSelect").appendChild(option);
            });
        }
    });

};
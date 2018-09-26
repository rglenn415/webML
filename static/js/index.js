var userData = {};

function parseFeatures(files){
    //selects the first file
    //possible to send many files, but for now we will only use one
    var data = Papa.parse(files[0],{
        complete: function(results){
            userData.file = results.data;
            // console.log('finished',results.data[0]);
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

function postUserData() {
    var selector = document.getElementById('featureSelect');
    userData.selectedFeature = selector.options[selector.selectedIndex].value;
    
    var request = {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(userData)
    }
    fetch("/postData", request).then(function(data) {
        return data.json()
    }).then(function(response) {
        console.log(response);
        document.getElementById('modelTrainingResultsSection').style.visibility = 'visible';
        document.getElementById('accuracy').innerHTML = response.accuracy;
        document.getElementById('confusionMatrix').innerHTML = response.confusion;
        document.getElementById('classificationReport').innerHTML = response.classification;
    });
}
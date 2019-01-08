//FIGURING A PATH FROM SOURCE TO DESTINATION

//CONFIG FILE
// A,B, 100
// B,C, 150
// C,D, 140

// A->D  
// pathToDestination(D,A,0)
// pathToDestination(C,A,140)
// pathToDestination(B,A,290)
// pathToDestination(A,A,390) -> 390


  A   B    C
A 0   100
B 100  0   150
C     150   0




var Destination_Source_Map = {};


function main(){
	createMap();
	var source = "A";
	var destination = "B";
	var distance = 0;
	var finalDistance = pathToDestination(source, destination, distance);
	if(finalDistance){
		return finalDistance;
	}else{
		return "No valid path";
	}
}


function createMap(configFile){
	var lines = read all lines from configFile
	lines.forEach(line=>{
		var source = line[0];
		var destination = line[1];
		var distance = line[2];
		Destination_Source_Map[destination] = {
			"source" : source,
			"distance" : distance
		};
	});
}


function pathToDestination(destination , finalSource, distance){
	let mapValue = Destination_Source_Map[destination] ? Destination_Source_Map[destination] : null;
	if(mapValue){
		currentSource = mapValue.source;
		currentDistance = mapValue.distance;
		distance = distance + currentDistance;
	} 
	
	if(currentSource == undefined){
		return null;
	}else
	{
		if(currentSource == finalSource){
			return distance;
		}else{
			return pathToDestination(currentSource, finalSource, distance);
		}
	}
}


function getSourceForDestination(destination){
//read from source-destination map
	source = Destination_Source_Map[destination] ? Destination_Source_Map[destination].source : null;
	distance =  Destination_Source_Map[destination] ? Destination_Source_Map[destination].distance : -1;
	return JSON.stringify({
		"source":source,
		"distance":distance,
	});
}
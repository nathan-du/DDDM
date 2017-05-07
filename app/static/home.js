/**
 * http://usejsdoc.org/
 */
$(document).ready(function(){
	//alert("This is Hello World by JQuery");
	console.log("Document is ready....");
	$('#resultSet').hide();
	$('#result-positive').hide();
	$('#result-negative').hide();
        $('#reason').hide();
	$('#idk').hide();
	
	$("#searchbutton").click(function(event){
		event.preventDefault();
		//alert("button clicked...!");
		checkFact();
	});

	var searchBox = document.getElementById("searchbox");
	searchBox.addEventListener("keydown", function (e) {
	if (e.keyCode === 13) {  //checks whether the pressed key is "Enter"
        	checkFact();
	}
});
	
});

function checkFact(){
	var query = "Pinakin";
	console.log(query);
	query = $('#searchbox').val();
	console.log("Inside check fact");
	console.log("Query Parameter: "+query);
	var url = "http://152.1.26.116:50000/test?query="+query;
	console.log(url);
	$.ajax({
		type : "GET",
		contentType : "application/json",
		url : url,
		//data : jQuery.param({ query: query}),
		dataType : 'json',
		timeout : 100000,
		success : function(data) {
			console.log("SUCCESS: ", data);
			console.log(data);
			show_result(data);
			//display(data);
		},
		error : function(e) {
			console.log("Ajax error occured....");
			console.log("ERROR: ", e);
			//display(e);
		},
		done : function(e) {
			//console.log("DONE");
		}
	});
}

function show_result(data){
	console.log("Inside show result");
	//var result = JSON.parse(data);
	var result = data;
	if(data.truth == null){
		$('#result-positive').removeClass("z-index");
		$('#result-positive').hide();
		
		$('#result-negative').removeClass("z-index");
		$('#result-negative').hide();

		$('#idk').addClass("z-index");
		$('#idk').show();
	}
        else if(data.truth){
		$('#result-negative').removeClass("z-index");
		$('#result-negative').hide();

		$('#idk').removeClass("z-index");
		$('#idk').hide();

		$('#result-positive').addClass("z-index");		
		$('#result-positive').show();
	}
	else{

		$('#result-positive').removeClass("z-index");
		$('#result-positive').hide();

		$('#idk').removeClass("z-index");
		$('#idk').hide();

		$('#result-negative').addClass("z-index");
		$('#result-negative').show();
	}

	var markup = result.reason;
	$("#reason").val(markup);
      //$("table tbody").append(markup);
	$("#reason").show();
}
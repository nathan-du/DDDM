/**
 * http://usejsdoc.org/
 */
$(document).ready(function(){
	//alert("This is Hello World by JQuery");
	console.log("Document is ready....");
	$("#searchbutton").click(function(event){
		event.preventDefault();
		alert("button clicked...!");
		checkFact();
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
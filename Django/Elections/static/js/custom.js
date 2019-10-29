$(document).ready(function(){

    		$("#add_number").click(function(e){

      			e.preventDefault();
      			var total_candidates = $("#number_candidates").val().trim();
      			if(total_candidates == "" || total_candidates <= 0){
        			alert("Need to define how many candidates");
      			}else{
					$("#add_number").hide();
					$("#number_candidates").hide();
					var x = '<h4 style="color: #ffffff">Candidate No-1</h4>';
					$("#dynamic_form").append('<div class="form-group"><label for="votetitle">Election Title</label><input class="form-control" type="text" name="v_title" id="votetitle" placeholder="Enter Election Title"/></div><hr/>');
					$("#dynamic_form").attr("action","/create-new-vote/"+total_candidates+"");
					for(i = 1; i<= total_candidates; i++){
						$("#dynamic_form").append('<div class="form-group"><label for="number_candidates">'+i+'. Candidate</label><input class="form-control" name="cadidate_id_'+i+'" id="number_candidates" type="number" placeholder="Enter Candidate - '+i+' ID"></div><div class="custom-file"><input type="file" class="custom-file-input" id="customFile" name="candidate_s_'+i+'"><label class="custom-file-label" for="customFile">Choose Candidate Sign</label></div><hr/>');
					}
					$("#dynamic_form").append('<a class="btn btn-info mr-3" href="#">Cancel</a><button type="submit" name="submit" class="btn btn-primary">Submit</button>');
      			}
    		});
		});
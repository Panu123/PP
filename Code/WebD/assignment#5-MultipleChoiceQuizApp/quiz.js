var allQuestions = null;
var xmlhttp = new XMLHttpRequest();
xmlhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
        allQuestions = JSON.parse(this.responseText);
        console.log(allQuestions);

        let currentPage = -1;
        let totalScore = 0;
        let review = false;

        $(document).ready(function () {
            $("#quiz").hide();
            $("#alert").hide();
            $("#nextBtn").html("Start Quiz");


            $("#nextBtn").click(function(){
                $("#nextBtn").html("Next");

                let answerArray = $("#myForm").serializeArray();

                
                if(answerArray.length==0 && currentPage>=0 && review==true) {
                    $("#alert").html("Please select an answer.");
                    $("#alert").fadeIn('fast');
                } else {
                    $("#alert").hide();

                    if(review) {
                        $("input[type=radio]").attr('disabled', true);
                        $(".a"+allQuestions[currentPage].correct).addClass("correct");
                        if(answerArray[0].value == allQuestions[currentPage].correct) {
                            totalScore++;
                        } else {
                         $(".a"+answerArray[0].value).addClass("wrong");
                        }

                        review = false;
                    } else {
                        $("#content").fadeOut('slow',function(){
                            currentPage++;
                            if(currentPage==allQuestions.length){

                                $("p").show();
                                $("#quiz").hide();
                                $("#nextBtn").hide();
                                $("p").html("You answered <span class='score'>"+totalScore+"/"+allQuestions.length+"</span> questions correctly!");
                            } else {
                                review = true;
                                let thisQ = allQuestions[currentPage];
                                
                                $("p").hide();
                                $("#quiz").show();
                                $("#form-question").html(thisQ.question);
                                $("#form-answers").empty();
                                let choiceArray = thisQ.choices;
                                for(let i=0; i<choiceArray.length; i++) {
                                    $("#form-answers").append('<div class="form-radio a'+i+'"><input type="radio" name="q'+currentPage+'" value="'+i+'"> ' + choiceArray[i] + '</div>');
                                }
                            }
                        });
                        $("#content").fadeIn('slow');
                    }

                }
            })
        });
        
    } 
};
xmlhttp.open("GET", "questions.json", true);
xmlhttp.send();
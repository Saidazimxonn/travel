jQuery(document).ready(function($){

    $.bvi();
    // alert(slang);

    function bvi_panel_voice(text) {
        if(Cookies.get('bvi-voice') === 'true'){
            if(responsiveVoice.voiceSupport()) {
                responsiveVoice.setDefaultVoice("Russian Female");
                // responsiveVoice.setDefaultVoice("Turkish Female");
                responsiveVoice.cancel();
                responsiveVoice.speak(text);
            }
        } else {
            responsiveVoice.cancel();
        }
    }

    $(function () {
        function getWordUnderCursor(event) {
            var range, textNode, offset;

            if (document.body.createTextRange) {           // Internet Explorer
                try {
                    range = document.body.createTextRange();
                    range.moveToPoint(event.clientX, event.clientY);
                    range.select();
                    range = getTextRangeBoundaryPosition(range, true);

                    textNode = range.node;
                    offset = range.offset;
                } catch(e) {
                    return "";
                }
            }
            else if (document.caretPositionFromPoint) {    // Firefox
                range = document.caretPositionFromPoint(event.clientX, event.clientY);
                textNode = range.offsetNode;
                offset = range.offset;
            } else if (document.caretRangeFromPoint) {     // Chrome
                range = document.caretRangeFromPoint(event.clientX, event.clientY);
                textNode = range.startContainer;
                offset = range.startOffset;
            }

            //data contains a full sentence
            //offset represent the cursor position in this sentence
            var data = textNode.data,
                i = offset,
                begin,
                end;

            //Find the begin of the word (space)
            while (i > 0 && data[i] !== "<") { --i; };
            begin = i;

            //Find the end of the word
            i = offset;
            while (i < data.length && data[i] !== ">") { ++i; };
            end = i;

            //Return the word under the mouse cursor
            return data.substring(begin, end);
        }

        //Get the HTML in a div #hoverText and detect mouse move on it
        var $hoverText = $(".body");
        $hoverText.mousemove(function (e) {
            var word = getWordUnderCursor(e);

            //Show the word in a div so we can test the result
            if (word !== ""){
                bvi_panel_voice(word);
                // $("#testResult").text(word);
            }

        });
    });

// This code make it works with IE
// REF: https://stackoverflow.com/questions/3127369/how-to-get-selected-textnode-in-contenteditable-div-in-ie
    function getTextRangeBoundaryPosition(textRange, isStart) {
        var workingRange = textRange.duplicate();
        workingRange.collapse(isStart);
        var containerElement = workingRange.parentElement();
        var workingNode = document.createElement("span");
        var comparison, workingComparisonType = isStart ?
            "StartToStart" : "StartToEnd";

        var boundaryPosition, boundaryNode;

        // Move the working range through the container's children, starting at
        // the end and working backwards, until the working range reaches or goes
        // past the boundary we're interested in
        do {
            containerElement.insertBefore(workingNode, workingNode.previousSibling);
            workingRange.moveToElementText(workingNode);
        } while ( (comparison = workingRange.compareEndPoints(
            workingComparisonType, textRange)) > 0 && workingNode.previousSibling);

        // We've now reached or gone past the boundary of the text range we're
        // interested in so have identified the node we want
        boundaryNode = workingNode.nextSibling;
        if (comparison == -1 && boundaryNode) {
            // This must be a data node (text, comment, cdata) since we've overshot.
            // The working range is collapsed at the start of the node containing
            // the text range's boundary, so we move the end of the working range
            // to the boundary point and measure the length of its text to get
            // the boundary's offset within the node
            workingRange.setEndPoint(isStart ? "EndToStart" : "EndToEnd", textRange);

            boundaryPosition = {
                node: boundaryNode,
                offset: workingRange.text.length
            };
        } else {
            // We've hit the boundary exactly, so this must be an element
            boundaryPosition = {
                node: containerElement,
                offset: getChildIndex(workingNode)
            };
        }

        // Clean up
        workingNode.parentNode.removeChild(workingNode);

        return boundaryPosition;
    }


});
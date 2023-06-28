$(document).ready(function(){

    // Load previously colored cells
    $.getJSON("/get_cells", function(data) {
        data.cells.forEach(function(cell) {
            $("#" + cell).css("background-color", "rgb(255, 0, 0)");
        });
    });

    // Click event to change color
    $("td").click(function() {

        // Check if cell is grey or red 
        var cell = $(this)
        var cell_color = cell.css("background-color");
        
        // change color accordingly
        if (cell_color == "rgb(255, 0, 0)") {
            cell.css('background-color', 'grey');
        } else {
            cell.css('background-color', 'rgb(255, 0, 0)');
        }

        // Save all red cells to database 
        $.ajax({
            url: "/save_cell",
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify({ 
                cell: $(this).attr("id"),
                color: cell.css("background-color")
         }),
            dataType: "json"
        });
    });

    // Reset all cells to grey
    $("#reset-button").click(function(data) {
        $("td").css("background-color", "grey");
        $.ajax({
            url: "/reset_cells",
            type: "POST",
            contentType: "application/json",
            data: JSON.stringify({ reset: true }),
            dataType: "json"
        });
    });
    
});


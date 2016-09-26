$( document ).ready(function() { // when resources load
  $(window).load(function() { // when html loads

    function customColsSameHeight(){
      // method that sets the same custom-col height to all the divs of the same class
      var customCol1 = ".custom-col:nth-of-type(1)";
      var customCol2 = ".custom-col:nth-of-type(2)";
      var customCol3 = ".custom-col:nth-of-type(3)";

      var h1 = $(customCol1).height(); // first .custom-col height
      var h2 = $(customCol2).height(); // second .custom-col height
      var h3 = $(customCol3).height(); // third .custom-col height

      var maxh = 0; // max height, all cols will have the same height

      if(maxh < h1){
        maxh = h1;
      }
      if(maxh < h2){
        maxh = h2;
      }
      if(maxh < h3){
        maxh = h3;
      }

      $(customCol1).height(maxh);
      $(customCol2).height(maxh);
      $(customCol3).height(maxh);
    }; // customColsSameHeight()

    customColsSameHeight();
  });
});

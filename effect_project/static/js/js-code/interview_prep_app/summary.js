jQuery( document ).ready(function() {
    $printBtn = ".print-btn.btn";
    $header = ".header";
    $printRow = ".print-row";


    function hideBeforePrint(){
      $($header).hide();
      $($printRow).hide();
    };

    function showAfterPrint(){
      $($header).show();
      $($printRow).show();
    };

    $(document).on('click', $printBtn, function(event){
        event.preventDefault();
        console.log('print button clicked');
        hideBeforePrint();
        print();
        showAfterPrint();
    });// click print the page
});

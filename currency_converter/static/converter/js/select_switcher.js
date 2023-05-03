$(document).ready(function() {
    var prevFromCurrency = $('#from_currency').val();
    var prevToCurrency = $('#to_currency').val();

    $('#from_currency, #to_currency').on('change', function() {
        var fromCurrency = $('#from_currency').val();
        var toCurrency = $('#to_currency').val();

        if (fromCurrency == toCurrency) {
            if (this.id == "from_currency") {
                $('#from_currency').val(prevToCurrency);
                $('#to_currency').val(prevFromCurrency);
            } else if (this.id == "to_currency") {
                $('#to_currency').val(prevFromCurrency);
                $('#from_currency').val(prevToCurrency);
            }
        }

        prevFromCurrency = $('#from_currency').val();
        prevToCurrency = $('#to_currency').val();
    });
});
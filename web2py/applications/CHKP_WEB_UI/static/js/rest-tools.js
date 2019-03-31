function send_to_beck(url,DTO) {
    var data = JSON.stringify(DTO);
    $.ajax({
        type: 'POST',
        url:url,
        scriptCharset:'utf-8',
        contentType:'application/json',
        data:data,
        dataType:'json',
        success: function (data) {
            return data;
        },
        error: function (data) {
            return false;
        }
    })
}
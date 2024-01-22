/*$(function(){
    $('.mask-cpfcnpj').mask('000.000.000-00', {reverse: true});
}); */

$(function(){
    function applyMask() {
    var documentoTipo = $('.mask-documento_tipo').val(); // Obtém o valor do campo de tipo de documento

        if (documentoTipo === 'CPF') {
            // Aplica a máscara de CPF
            $('.mask-cpfcnpj').mask('000.000.000-00', {reverse: true});
        } else if (documentoTipo === 'CNPJ') {
            // Aplica a máscara de CNPJ
            $('.mask-cpfcnpj').mask('00.000.000/0000-00', {reverse: true});
        } else {
            // Remove qualquer máscara existente se o tipo de documento não for escolhido
            $('.mask-cpfcnpj').unmask();
        }
    }
    
    // Chama a função quando a página carrega e sempre que o tipo de documento muda
    $('.mask-documento_tipo').change(applyMask);
    applyMask();  // Chama a função na inicialização
    });

/*
$(document).ready(function () {
    // Função para aplicar a máscara de CPF ou CNPJ
    function applyMask() {
        var documentoTipo = $('#id_documento_tipo').val(); // Obtém o valor do campo de tipo de documento

        if (documentoTipo === 'CPF') {
            // Aplica a máscara de CPF
            $('#id_documento_numero').mask('000.000.000-00', {reverse: true});
        } else if (documentoTipo === 'CNPJ') {
            // Aplica a máscara de CNPJ
            $('#id_documento_numero').mask('00.000.000/0000-00', {reverse: true});
        } else {
            // Remove qualquer máscara existente se o tipo de documento não for escolhido
            $('#id_documento_numero').unmask();
        }
    }

    // Chama a função quando a página carrega e sempre que o tipo de documento muda
    $('#id_documento_tipo').change(applyMask);
    applyMask();  // Chama a função na inicialização
});

*/



# -*- coding: utf-8 -*-

from openerp.osv import fields, osv
import logging
_logger = logging.getLogger(__name__)

class funciones1(osv.osv):

    def numero_silabas(self, cr, uid, ids, field_name, arg, context=None):
        registros = self.browse(cr, uid, ids)
        resultado = {}
        for r in registros:
           resultado[r.id] = r.importe1 * r.importe2
        print "RESULTADO: ", resultado
        msg = "Error David1 : " % resultado
        _logger.error(msg)
	return resultado
	
    def calcular_display1(self, cr, uid, ids, field_name, arg, context=None):
        registros = self.browse(cr, uid, ids)
        resultado = {}
        for r in registros:
           resultado[r.id] = r.importe1 - r.importe2
        print "RESULTADO: ", resultado
        msg = "Error David2 : " % resultado
        _logger.error(msg)
	return resultado

    _name = 'funciones1'
    _columns = {
        'palabra': fields.char('Palabra', size=200, required=False),
        'silabas': fields.function (numero_silabas, type = 'integer', string = 'Numero Silabas', store = False),
		'display1': fields.function (calcular_display1, type = 'float', string = 'Display1', store = False),
    }
funciones1()

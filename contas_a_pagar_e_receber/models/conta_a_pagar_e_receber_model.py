from sqlalchemy import Column, Integer, String, Numeric, ForeignKey
from sqlalchemy.orm import relationship

from shared.database import Base


class ContaPagarReceber(Base):
    __tablename__ = 'contas_a_pagar_e_receber'

    id = Column(Integer, primary_key=True, autoincrement=True)
    descricao = Column(String(30))
    valor = Column(Numeric(10,2))
    tipo = Column(String(30))

    fornecedor_cliente_id = Column(Integer, ForeignKey("fornecedor_cliente.id"), nullable=False)
    fornecedor = relationship("FornecedorCliente")


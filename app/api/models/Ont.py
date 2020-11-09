"""
Models for the Api app
"""

# local imports
from ...config.db import db
from flask_serialize import FlaskSerializeMixin

FlaskSerializeMixin.db = db

class Ont(FlaskSerializeMixin, db.Model):
	"""
	This class represents the ont table.
	"""

	# Ensures table will be named in plural and not in singular as in
	# the name of the model
	__tablename__ = 'olt_ont'

	Code = db.Column(db.String(length=250), primary_key=True)
	HostCode = db.Column(db.String(length=250))
	Sn = db.Column(db.String(length=250))
	Version = db.Column(db.String(length=250))
	SoftwareVersion = db.Column(db.String(length=250))
	EquipmentId = db.Column(db.String(length=250))
	FrameId = db.Column(db.String(length=250))
	SlotId = db.Column(db.String(length=250))
	PortId = db.Column(db.String(length=250))
	ActiveStatus = db.Column(db.Integer)
	CreatedBy = db.Column(db.DateTime, index=True, server_default=db.func.now())
	CreatedDate = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())
	UpdatedBy = db.Column(db.DateTime, index=True, server_default=db.func.now())
	UpdatedDate = db.Column(db.DateTime, server_default=db.func.now(), onupdate=db.func.now())

	def __repr__(self):
		return '<Code: {}>'.format(self.Code)

	def list(self):
		onts = Ont.query.all()
		return Ont.json_list(onts)

	def show(self):
		Ont.query.get(Code=self.Code)

	def save(self):
		db.session.add(self)
		db.session.commit()

	def update(self):
		db.session.add(self)
		db.session.commit()

	def delete(self):
		Ont.query.filter_by(Code=self.Code).delete()

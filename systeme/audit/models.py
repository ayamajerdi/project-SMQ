from django.db import models
from django.contrib.auth.models import User
from doc.models import DocExt

class Audit(models.Model):

    reference_audit = models.CharField(max_length=100) 
    demandeur = models.ForeignKey(User, on_delete=models.CASCADE)  
    designation = models.TextField() 
    champ_audit = models.ManyToManyField(User, related_name='audits_access', limit_choices_to={'groups__name': 'audit'}) 
    type_audit = models.CharField(max_length=100) 
    auditeurs = models.ManyToManyField(User, related_name='audits_auditors', limit_choices_to={'groups__name': 'Employe'})
    date_debut_audit = models.DateField() 
    date_fin_audit = models.DateField()  
    document_reference = models.ForeignKey(DocExt,on_delete=models.CASCADE, related_name='audits_auditors')
    audités = models.ManyToManyField(User, related_name='audits_audited') 
    responsable_validation = models.ForeignKey(User, on_delete=models.CASCADE, related_name='audits_validator', limit_choices_to={'groups__name': 'Employe'})  
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='audit_updated', null=True)
    created_at = models.DateTimeField(null=True, default=None)
    updated_at = models.DateTimeField(null=True, default=None)

    def __str__(self):
        return self.reference_audit
    

class PlanAudit(models.Model):
    audit = models.ForeignKey(Audit, on_delete=models.CASCADE) 
    designation = models.TextField() 
    date = models.DateField()  
    heure_debut = models.IntegerField()  
    heure_fin = models.IntegerField() 
    lieu = models.CharField(max_length=100)  
    commentaires = models.TextField()  
    personnes_concernees = models.ManyToManyField(User, related_name='personnes_concernees', limit_choices_to={'groups__name': 'Employe'})
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='plan_audit_created', limit_choices_to={'groups__name': 'redacteur'})
    updated_by = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='plan_audit_updated', null=True)
    created_at = models.DateTimeField(null=True, default=None)
    updated_at = models.DateTimeField(null=True, default=None)

    def __str__(self):
        return self.designation


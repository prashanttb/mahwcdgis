from django.db import models
# from django.contrib.gis.db import models

# Create your models here.
class RuralInfraAwcAcEnglishconverted(models.Model):
    geom = models.TextField(blank=True, null=True)
    awc_code = models.CharField(max_length=254, blank=True, null=True)
    district = models.CharField(max_length=254, blank=True, null=True)
    project = models.CharField(max_length=254, blank=True, null=True)
    beat = models.CharField(max_length=254, blank=True, null=True)
    latitude = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    longitude = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    altitude = models.CharField(max_length=254, blank=True, null=True)
    accuracy = models.CharField(max_length=254, blank=True, null=True)
    objectid = models.BigIntegerField(blank=True, null=True)
    st_code = models.BigIntegerField(blank=True, null=True)
    st_name = models.CharField(max_length=254, blank=True, null=True)
    dist_code = models.BigIntegerField(blank=True, null=True)
    dist_name = models.CharField(max_length=254, blank=True, null=True)
    ac_no = models.BigIntegerField(blank=True, null=True)
    ac_name = models.CharField(max_length=254, blank=True, null=True)
    start = models.DateField(blank=True, null=True)
    end = models.DateField(blank=True, null=True)
    division = models.CharField(max_length=254, blank=True, null=True)
    district_1 = models.CharField(max_length=254, blank=True, null=True)
    project_2 = models.CharField(max_length=254, blank=True, null=True)
    beat_3 = models.CharField(max_length=254, blank=True, null=True)
    anganwadi_field = models.CharField(db_column='anganwadi_', max_length=254, blank=True, null=True)  # Field renamed because it ended with '_'.
    agan_type = models.CharField(max_length=254, blank=True, null=True)
    agancbuil_field = models.CharField(db_column='agancbuil_', max_length=254, blank=True, null=True)  # Field renamed because it ended with '_'.
    aganc_forr = models.CharField(max_length=254, blank=True, null=True)
    yes_moveag = models.CharField(max_length=254, blank=True, null=True)
    no_owner_a = models.CharField(max_length=254, blank=True, null=True)
    child_sita = models.CharField(max_length=254, blank=True, null=True)
    child_weig = models.CharField(max_length=254, blank=True, null=True)
    child_we_1 = models.CharField(max_length=254, blank=True, null=True)
    adult_wteq = models.CharField(max_length=254, blank=True, null=True)
    adult_wt_1 = models.CharField(max_length=254, blank=True, null=True)
    infant_met = models.CharField(max_length=254, blank=True, null=True)
    infant_m_1 = models.CharField(max_length=254, blank=True, null=True)
    stadiomete = models.CharField(max_length=254, blank=True, null=True)
    stadm_work = models.CharField(max_length=254, blank=True, null=True)
    maint_repa = models.CharField(max_length=254, blank=True, null=True)
    agan_drink = models.CharField(max_length=254, blank=True, null=True)
    agan_tap = models.CharField(max_length=254, blank=True, null=True)
    plumb_work = models.CharField(max_length=254, blank=True, null=True)
    toil_fac = models.CharField(max_length=254, blank=True, null=True)
    toil_worki = models.CharField(max_length=254, blank=True, null=True)
    electricit = models.CharField(max_length=254, blank=True, null=True)
    solar_powe = models.CharField(max_length=254, blank=True, null=True)
    agan_tv = models.CharField(max_length=254, blank=True, null=True)
    tv_working = models.CharField(max_length=254, blank=True, null=True)
    agan_fenc = models.CharField(max_length=254, blank=True, null=True)
    agan_back_field = models.CharField(db_column='agan_back_', max_length=254, blank=True, null=True)  # Field renamed because it ended with '_'.
    space_own_field = models.CharField(db_column='space_own_', max_length=254, blank=True, null=True)  # Field renamed because it ended with '_'.
    vac_agan = models.CharField(max_length=254, blank=True, null=True)
    post_vac = models.CharField(max_length=254, blank=True, null=True)
    post_vac_a = models.BigIntegerField(blank=True, null=True)
    post_vac_h = models.BigIntegerField(blank=True, null=True)
    pro_fill_a = models.CharField(max_length=254, blank=True, null=True)
    child0_6mo = models.BigIntegerField(blank=True, null=True)
    child6mon_field = models.BigIntegerField(db_column='child6mon_', blank=True, null=True)  # Field renamed because it ended with '_'.
    child3_6y = models.BigIntegerField(db_column='child3 _6y', blank=True, null=True)  # Field renamed to remove unsuitable characters.
    tot_no_chi = models.BigIntegerField(blank=True, null=True)
    preg_moth_field = models.BigIntegerField(db_column='preg_moth_', blank=True, null=True)  # Field renamed because it ended with '_'.
    brestfeed_field = models.BigIntegerField(db_column='brestfeed_', blank=True, null=True)  # Field renamed because it ended with '_'.
    preg_lact_field = models.BigIntegerField(db_column='preg_lact_', blank=True, null=True)  # Field renamed because it ended with '_'.
    aadh_notli = models.BigIntegerField(blank=True, null=True)
    preg_lac_1 = models.BigIntegerField(blank=True, null=True)
    child_we_2 = models.BigIntegerField(blank=True, null=True)
    child_heig = models.BigIntegerField(blank=True, null=True)
    no_suv_chi = models.BigIntegerField(blank=True, null=True)
    no_suv_c_1 = models.BigIntegerField(blank=True, null=True)
    child_sam_field = models.BigIntegerField(db_column='child_sam_', blank=True, null=True)  # Field renamed because it ended with '_'.
    child_rec_field = models.CharField(db_column='child_rec_', max_length=254, blank=True, null=True)  # Field renamed because it ended with '_'.
    sam_child_field = models.BigIntegerField(db_column='sam_child_', blank=True, null=True)  # Field renamed because it ended with '_'.
    sam_agan_n = models.CharField(max_length=254, blank=True, null=True)
    no_adol_gi = models.BigIntegerField(blank=True, null=True)
    child_agan = models.CharField(max_length=254, blank=True, null=True)
    ifyes_chil = models.BigIntegerField(blank=True, null=True)
    agan_rec_m = models.CharField(max_length=254, blank=True, null=True)
    bene_agan_field = models.BigIntegerField(db_column='bene_agan_', blank=True, null=True)  # Field renamed because it ended with '_'.
    agan_bene_field = models.BigIntegerField(db_column='agan_bene_', blank=True, null=True)  # Field renamed because it ended with '_'.
    benetot_mi = models.CharField(max_length=254, blank=True, null=True)
    migrbeneto = models.BigIntegerField(blank=True, null=True)
    agan_serv_field = models.CharField(db_column='agan_serv_', max_length=254, blank=True, null=True)  # Field renamed because it ended with '_'.
    ifyes_agan = models.CharField(max_length=254, blank=True, null=True)
    ifyes_gp_s = models.CharField(max_length=254, blank=True, null=True)
    aay = models.CharField(max_length=254, blank=True, null=True)
    totno_chil = models.CharField(max_length=254, blank=True, null=True)
    preg_lac_2 = models.CharField(max_length=254, blank=True, null=True)
    parvisit_i = models.CharField(max_length=254, blank=True, null=True)
    parent_vis = models.CharField(max_length=254, blank=True, null=True)
    balasch = models.BigIntegerField(blank=True, null=True)
    agan_und_b = models.CharField(max_length=254, blank=True, null=True)
    work_comun = models.CharField(max_length=254, blank=True, null=True)
    ifcom_ongo = models.CharField(max_length=254, blank=True, null=True)
    ifcom_on_1 = models.BigIntegerField(blank=True, null=True)
    ifcom_on_2 = models.CharField(max_length=254, blank=True, null=True)
    ifcom_on_3 = models.BigIntegerField(blank=True, null=True)
    ifcom_on_4 = models.BigIntegerField(blank=True, null=True)
    ifcom_on_5 = models.BigIntegerField(blank=True, null=True)
    sign_sup_c = models.CharField(max_length=254, blank=True, null=True)
    sign_sup_h = models.CharField(max_length=254, blank=True, null=True)
    field_id = models.BigIntegerField(db_column='_id', blank=True, null=True)  # Field renamed because it started with '_'.
    field_uuid = models.CharField(db_column='_uuid', max_length=254, blank=True, null=True)  # Field renamed because it started with '_'.
    field_submissio = models.CharField(db_column='_submissio', max_length=254, blank=True, null=True)  # Field renamed because it started with '_'.
    field_validatio = models.CharField(db_column='_validatio', max_length=254, blank=True, null=True)  # Field renamed because it started with '_'.
    field_notes = models.CharField(db_column='_notes', max_length=254, blank=True, null=True)  # Field renamed because it started with '_'.
    field_status = models.CharField(db_column='_status', max_length=254, blank=True, null=True)  # Field renamed because it started with '_'.
    field_submitted = models.CharField(db_column='_submitted', max_length=254, blank=True, null=True)  # Field renamed because it started with '_'.
    field_tags = models.CharField(db_column='_tags', max_length=254, blank=True, null=True)  # Field renamed because it started with '_'.
    field_index = models.BigIntegerField(db_column='_index', blank=True, null=True)  # Field renamed because it started with '_'.
    field_108 = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rural_infra_awc_ac_englishconverted'
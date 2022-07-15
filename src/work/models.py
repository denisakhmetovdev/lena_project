from django.db import models


class Contractor(models.Model):
    title = models.CharField(max_length=255, verbose_name='Контрагент')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Контрагент'
        verbose_name_plural = 'Контрагенты'


class Company(models.Model):
    title = models.CharField(max_length=255, verbose_name='Компания')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'


class ProjectManager(models.Model):
    first_name = models.CharField(max_length=40, verbose_name='Имя')
    last_name = models.CharField(max_length=40, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=50, null=True, blank=True, verbose_name='Отчество')

    def get_full_name(self):
        if self.patronymic:
            full_name = f'{self.last_name} {self.first_name} {self.patronymic}'
        else:
            full_name = f'{self.last_name} {self.first_name}'
        return full_name

    def __str__(self):
        return self.get_full_name()

    class Meta:

        verbose_name = 'ПМ'
        verbose_name_plural = 'ПМ\'ы'


class Contract(models.Model):
    RISKS = [
        (1, 'Какой-то риск 1'),
        (2, 'Какой-то риск 2'),
        (3, 'Какой-то риск 3'),
        (4, 'Какой-то риск 4'),
        (5, 'Какой-то риск 5'),
        (6, 'Какой-то риск 6'),
        (7, 'Какой-то риск 7'),
        (8, 'Какой-то риск 8'),
        (9, 'Какой-то риск 9')
    ]

    STATUSES = [
        (1, 'status 1'),
        (2, 'status 2'),
        (3, 'status 3'),
        (4, 'status 4'),
        (5, 'status 5'),
    ]

    cipher = models.CharField(max_length=25, verbose_name='Шифр')
    is_in_ISUP = models.BooleanField(verbose_name='Наличие в ИСУП', help_text='Возможно стоило сделать поле текстовым')
    number_DS = models.CharField(max_length=25, verbose_name='Номер ДС')
    DS_date = models.DateField(verbose_name='Дата ДС')
    transit = models.CharField(max_length=30, verbose_name='Транзит', help_text='Не знаю что это, возможно стоило '
                                                                                'сделать поле Да/Нет')
    about_contract = models.CharField(max_length=255, verbose_name='Предмет договора')
    risks = models.PositiveSmallIntegerField(('risks'), choices=RISKS)
    vat = models.DecimalField(decimal_places=2, max_digits=13, verbose_name='Сумма НДС')
    start_date = models.DateField(verbose_name='Дата заключения договора')
    end_date = models.DateField(verbose_name='Срок действия договора')
    work_completion_time = models.DateField(verbose_name='Срок исполнения работ по договору')
    completion_date = models.DateField(verbose_name='Дата завершения работ')
    main_status = models.PositiveSmallIntegerField(('main_status'), choices=STATUSES)
    money_receipt = models.DateField(verbose_name='Дата поступления денег')
    actual_performance = models.DateField(verbose_name='Дата фактического исполнения')
    risks_signs = models.CharField(max_length=255, verbose_name='Проявление рисков')
    reaction = models.CharField(max_length=255, verbose_name='Меры реагирования при проявлении рисков')
    contractor = models.ForeignKey(Contractor, on_delete=models.CASCADE, verbose_name='Контрагент')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='Компания')
    manager = models.ForeignKey(ProjectManager, on_delete=models.PROTECT, verbose_name='ПМ')

    def __str__(self):
        return f'{self.about_contract} ---- {self.contractor}'

    class Meta:

        verbose_name = 'Договор'
        verbose_name_plural = 'Договоры'


class MonthStatus(models.Model):
    """
    Не понял, что за поле "Исполнение",
    поэтому сделал его Charfield
    """

    performance = models.CharField(max_length=255, verbose_name='Исполнение')
    date = models.DateField(verbose_name='Дата')
    certificate_of_completion = models.BooleanField(default=False, verbose_name='АВР')
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, verbose_name='Договор')

    def __str__(self):
        return 'Есть АВР' if self.certificate_of_completion else 'Нет АВР'

    class Meta:
        verbose_name = 'Статус за месяц'
        verbose_name_plural = 'Статусы за месяц'


class Status(models.Model):

    comment = models.TextField(verbose_name='Комментарий')
    date = models.DateField(auto_now=True, verbose_name='Дата комментария')
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, verbose_name='Договор')

    def __str__(self):
        return self.comment

    class Meta:

        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'


class SupplementaryContract(models.Model):
    title = models.CharField(max_length=255, verbose_name='Наименование доп. договора')
    data = models.DateField(verbose_name='Доп. договор от:')
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, verbose_name='К договору')

    def get_short_title(self):
        if len(self.title) > 20:
            short_title = self.title[:20]
        else:
            short_title = self.title
        return short_title

    def __str__(self):
        return self.get_short_title()

    class Meta:

        verbose_name = 'Доп. договор'
        verbose_name_plural = 'Доп. договоры'

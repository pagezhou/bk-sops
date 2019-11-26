# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云PaaS平台社区版 (BlueKing PaaS Community
Edition) available.
Copyright (C) 2017-2019 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at
http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.
"""



from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statistics', '0007_init_pipeline_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instanceinpipeline',
            name='atom_total',
            field=models.IntegerField(verbose_name='\u539f\u5b50\u603b\u6570'),
        ),
        migrations.AlterField(
            model_name='instanceinpipeline',
            name='gateways_total',
            field=models.IntegerField(verbose_name='\u7f51\u5173\u603b\u6570'),
        ),
        migrations.AlterField(
            model_name='instanceinpipeline',
            name='instance_id',
            field=models.CharField(max_length=255, verbose_name='\u5b9e\u4f8bID'),
        ),
        migrations.AlterField(
            model_name='instanceinpipeline',
            name='subprocess_total',
            field=models.IntegerField(verbose_name='\u5b50\u6d41\u7a0b\u603b\u6570'),
        ),
        migrations.AlterField(
            model_name='templateinpipeline',
            name='atom_total',
            field=models.IntegerField(verbose_name='\u539f\u5b50\u603b\u6570'),
        ),
        migrations.AlterField(
            model_name='templateinpipeline',
            name='gateways_total',
            field=models.IntegerField(verbose_name='\u7f51\u5173\u603b\u6570'),
        ),
        migrations.AlterField(
            model_name='templateinpipeline',
            name='subprocess_total',
            field=models.IntegerField(verbose_name='\u5b50\u6d41\u7a0b\u603b\u6570'),
        ),
        migrations.AlterField(
            model_name='templateinpipeline',
            name='template_id',
            field=models.CharField(max_length=255, verbose_name='\u6a21\u677fID'),
        ),
    ]

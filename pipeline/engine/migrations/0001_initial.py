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
# Generated by Django 1.11.2 on 2017-11-24 10:43


from django.db import migrations, models
import django.db.models.deletion
import pipeline.engine.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.CharField(max_length=32, primary_key=True, serialize=False, unique=True, verbose_name='\u8282\u70b9 ID')),
                ('inputs', pipeline.engine.models.IOField(verbose_name='\u8f93\u5165\u6570\u636e')),
                ('outputs', pipeline.engine.models.IOField(verbose_name='\u8f93\u51fa\u6570\u636e')),
                ('ex_data', pipeline.engine.models.IOField(verbose_name='\u5f02\u5e38\u6570\u636e')),
            ],
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(db_index=True, max_length=32, verbose_name='\u8282\u70b9 id')),
                ('started_time', models.DateTimeField(verbose_name='\u5f00\u59cb\u65f6\u95f4')),
                ('archived_time', models.DateTimeField(verbose_name='\u7ed3\u675f\u65f6\u95f4')),
            ],
        ),
        migrations.CreateModel(
            name='HistoryData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inputs', pipeline.engine.models.IOField(verbose_name='\u8f93\u5165\u6570\u636e')),
                ('outputs', pipeline.engine.models.IOField(verbose_name='\u8f93\u51fa\u6570\u636e')),
                ('ex_data', pipeline.engine.models.IOField(verbose_name='\u5f02\u5e38\u6570\u636e')),
            ],
        ),
        migrations.CreateModel(
            name='NodeRelationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ancestor_id', models.CharField(db_index=True, max_length=32, verbose_name='\u7956\u5148 ID')),
                ('descendant_id', models.CharField(db_index=True, max_length=32, verbose_name='\u540e\u4ee3 ID')),
                ('distance', models.IntegerField(verbose_name='\u8ddd\u79bb')),
            ],
        ),
        migrations.CreateModel(
            name='PipelineModel',
            fields=[
                ('id', models.CharField(max_length=32, primary_key=True, serialize=False, unique=True, verbose_name='pipeline ID')),
            ],
        ),
        migrations.CreateModel(
            name='PipelineProcess',
            fields=[
                ('id', models.CharField(max_length=32, primary_key=True, serialize=False, unique=True, verbose_name='Process ID')),
                ('root_pipeline_id', models.CharField(max_length=32, verbose_name='\u6839 pipeline \u7684 ID')),
                ('current_node_id', models.CharField(db_index=True, default=b'', max_length=32, verbose_name='\u5f53\u524d\u63a8\u8fdb\u5230\u7684\u8282\u70b9\u7684 ID')),
                ('destination_id', models.CharField(default=b'', max_length=32, verbose_name='\u9047\u5230\u8be5 ID \u7684\u8282\u70b9\u5c31\u505c\u6b62\u63a8\u8fdb')),
                ('parent_id', models.CharField(default=b'', max_length=32, verbose_name='\u7236 process \u7684 ID')),
                ('ack_num', models.IntegerField(default=0, verbose_name='\u6536\u5230\u5b50\u8282\u70b9 ACK \u7684\u6570\u91cf')),
                ('need_ack', models.IntegerField(default=-1, verbose_name='\u9700\u8981\u6536\u5230\u7684\u5b50\u8282\u70b9 ACK \u7684\u6570\u91cf')),
                ('is_alive', models.BooleanField(default=True, verbose_name='\u8be5 process \u662f\u5426\u8fd8\u6709\u6548')),
                ('is_sleep', models.BooleanField(default=False, verbose_name='\u8be5 process \u662f\u5426\u6b63\u5728\u4f11\u7720')),
            ],
        ),
        migrations.CreateModel(
            name='ProcessCeleryTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('process_id', models.CharField(db_index=True, max_length=32, unique=True, verbose_name='pipeline \u8fdb\u7a0b ID')),
                ('celery_task_id', models.CharField(default=b'', max_length=40, verbose_name='celery \u4efb\u52a1 ID')),
            ],
        ),
        migrations.CreateModel(
            name='ProcessSnapshot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', pipeline.engine.models.IOField(verbose_name='\u5b50 process ID \u4e0e pipeline_stack')),
            ],
        ),
        migrations.CreateModel(
            name='ScheduleService',
            fields=[
                ('id', models.CharField(max_length=64, primary_key=True, serialize=False, unique=True, verbose_name='ID \u8282\u70b9ID+version')),
                ('activity_id', models.CharField(db_index=True, max_length=32, verbose_name='\u8282\u70b9 ID')),
                ('process_id', models.CharField(max_length=32, verbose_name='Pipeline \u8fdb\u7a0b ID')),
                ('schedule_times', models.IntegerField(default=0, verbose_name='\u88ab\u8c03\u5ea6\u6b21\u6570')),
                ('wait_callback', models.BooleanField(default=False, verbose_name='\u662f\u5426\u662f\u56de\u8c03\u578b\u8c03\u5ea6')),
                ('callback_data', pipeline.engine.models.IOField(default=None, verbose_name='\u56de\u8c03\u6570\u636e')),
                ('service_act', pipeline.engine.models.IOField(verbose_name='\u5f85\u8c03\u5ea6\u670d\u52a1')),
                ('is_finished', models.BooleanField(default=False, verbose_name='\u662f\u5426\u5df2\u5b8c\u6210')),
                ('version', models.CharField(db_index=True, max_length=32, verbose_name='Activity \u7684\u7248\u672c')),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.CharField(max_length=32, primary_key=True, serialize=False, unique=True, verbose_name='\u8282\u70b9 ID')),
                ('state', models.CharField(max_length=10, verbose_name='\u72b6\u6001')),
                ('name', models.CharField(default=b'', max_length=64, verbose_name='\u8282\u70b9\u540d\u79f0')),
                ('retry', models.IntegerField(default=0, verbose_name='\u91cd\u8bd5\u6b21\u6570')),
                ('loop', models.IntegerField(default=1, verbose_name='\u5faa\u73af\u6b21\u6570')),
                ('skip', models.BooleanField(default=False, verbose_name='\u662f\u5426\u8df3\u8fc7')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('started_time', models.DateTimeField(null=True, verbose_name='\u5f00\u59cb\u65f6\u95f4')),
                ('archived_time', models.DateTimeField(null=True, verbose_name='\u5f52\u6863\u65f6\u95f4')),
                ('version', models.CharField(max_length=32, verbose_name='\u7248\u672c')),
            ],
            options={
                'ordering': ['-created_time'],
            },
        ),
        migrations.CreateModel(
            name='SubProcessRelationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subprocess_id', models.CharField(db_index=True, max_length=32, verbose_name='\u5b50\u6d41\u7a0b ID')),
                ('process_id', models.CharField(max_length=32, verbose_name='\u5bf9\u5e94\u7684\u8fdb\u7a0b ID')),
            ],
        ),
        migrations.AddField(
            model_name='pipelineprocess',
            name='snapshot',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='engine.ProcessSnapshot'),
        ),
        migrations.AddField(
            model_name='pipelinemodel',
            name='process',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='engine.PipelineProcess'),
        ),
        migrations.AddField(
            model_name='history',
            name='data',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='engine.HistoryData'),
        ),
    ]
